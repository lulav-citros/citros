from io import StringIO
from rosbags.rosbag2 import Reader
from pathlib import Path
from rosbags.serde import deserialize_cdr
import logging
import json
from .reader_parser import Parser
import numpy as np
import os

CHUNK_SIZE = 50 * 1024 * 1024

###############
##### PG ######
###############


class NumpyEncoder(json.JSONEncoder):
    """
        Overrides the default() method to handle NumPy arrays.
        
        Parameters:
        -----------
        obj : object
            Object to be serialized.
            
        Returns:
        --------
        list or object
            If obj is a NumPy array, returns a list containing the elements of the array.
            Otherwise, returns the result of the default JSONEncoder's default method.
    """
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)


class BagReaderCustomMessages():

    """
        Custom reader for ROS bag files with support for specialized message types.
        
        This class is responsible for reading messages from ROS bag files and serializing
        them into JSON format. It handles a variety of message types, including custom ones,
        and manages various complexities like nested message structures and special values.
        
        Attributes:
        -----------
        log : Logger
            A logging object for capturing runtime information.
        parser : Parser
            A parser object used to convert deserialized ROS messages to dictionary format.
        unsupported_topics : list
            A list to keep track of unsupported topics encountered during processing.
        
        Methods:
        --------
        sanitize_json(message_json: dict) -> dict:
            Sanitizes the JSON object by replacing certain special values like 'NaN' and 'Infinity'.
            
        handle_tf_msgs(msg: dict) -> dict:
            Handles transformation messages, reshaping them for easier processing.
            
        read_messages(input_bag: str, simulation_run_id: int) -> StringIO:
            Reads messages from a ROS bag file, serializes them into JSON, and writes them to a buffer.
            
        Example Usage:
        --------------
        >>> reader = BagReaderCustomMessages('path/to/custom/messages')
        >>> buffer = reader.read_messages('path/to/bagfile.bag', 1)
    """

    def __init__(self, custom_message_path):
        logging.basicConfig(
            level=logging.DEBUG,
            format='[%(asctime)s.%(msecs)03d][%(funcName)s][%(levelname)s] %(message)s',
            datefmt='%H:%M:%S'
        )

        self.log = logging.getLogger('Uploader')
        self.log.setLevel(logging.DEBUG)
        self.log.debug(f"custom_message_path = {custom_message_path}")
        self.parser = Parser(custom_message_path)

        self.unsupported_topics = []

    @staticmethod
    def sanitize_json(message_json: dict) -> dict:
        if "NaN" in message_json:
            message_json = message_json.replace("NaN", "-1")
        if "Infinity" in message_json:
            message_json = message_json.replace("Infinity", "-1")
        if "<?xml version=" in message_json:  # robot description topic
            message_json = json.dumps(
                {"error": "robot description not supported yet ..."})
        return message_json

    @staticmethod
    def handle_tf_msgs(msg: dict) -> dict:
        message_dict = {}
        for tf in msg['transforms']:
            message_dict[tf.header.frame_id] = {"header": str(tf.header),
                                                "__msgtype__": tf.__msgtype__,
                                                "translation": [tf.transform.translation.x, tf.transform.translation.y, tf.transform.translation.z],
                                                "rotation": [tf.transform.rotation.x, tf.transform.rotation.y, tf.transform.rotation.z, tf.transform.rotation.w]}
        return message_dict

    def read_messages(self, input_bag: str, simulation_run_id: int) -> StringIO:
        buffer = StringIO()
        size = 0
        rid = 0

        file_extension = input_bag.split(".")[1]
        self.log.debug(f"sqlite3 bag detected, {input_bag}") if file_extension != "mcap" else self.log.debug(
            f"mcap bag detected, {input_bag}")
        input_bag = os.path.dirname(input_bag)

        with Reader(Path(input_bag)) as reader:
            connections = [x for x in reader.connections if x.topic not in [
                "/rosout", "/client_count", "/connected_clients"]]
            for connection, timestamp, raw_data in reader.messages(connections=connections):

                if connection.msgtype == "rcl_interfaces/msg/ParameterEvent":  # ignoring parameter event topic
                    continue

                try:
                    message_deserialized = deserialize_cdr(
                        raw_data, connection.msgtype)
                    message_dict = self.parser.deserialized_message_to_dict(
                        message_deserialized)
                except KeyError as e:  # unregister message type, skipping
                    if connection.topic not in self.unsupported_topics:
                        self.log.warning(
                            f"[KeyError] skipping topic: {connection.topic} because unsupported message type: {connection.msgtype}, if nested, unknown: {str(e)}")
                        self.unsupported_topics.append(connection.topic)
                    continue

                except AssertionError as e:
                    self.log.warning(
                            f"[AssertionError]: skipping topic: {connection.topic} because unsupported message type: {connection.msgtype}, if nested, unknown: {str(e)}")
                    continue

                if "Multi" in connection.msgtype:  # message type is MultiArray, take only data and __msgtype__
                    message_dict = {k: message_dict[k] for k in message_dict.keys() & {
                        'data', '__msgtype__'}}

                if "sensor_msgs/msg/Image" in connection.msgtype:
                    self.log.warning("Image message detected ...")
                    continue

                if "tf2_msgs/msg/TFMessage" in connection.msgtype:
                    message_dict = self.handle_tf_msgs(message_dict)

                try:  # parse message
                    message_json = json.dumps(message_dict, cls=NumpyEncoder)
                except Exception:
                    try:  # nested message, try to flatten it
                        message_dict = self.parser.flatten_dict(message_dict)
                        message_dict = self.parser.nest_dict(message_dict)
                        message_json = json.dumps(
                            message_dict, cls=NumpyEncoder)
                    except Exception:  # can't flatten the message, need further inspection
                        if connection.topic not in self.unsupported_topics:
                            self.log.warning(
                                f"ignoring topic: {connection.topic}, with type: {connection.msgtype}")
                            self.unsupported_topics.append(connection.topic)
                        continue

                message_json = self.sanitize_json(message_json)

                try:
                    row = chr(0x1E).join([f"{simulation_run_id}", f"{rid}", f"{timestamp}",
                                          f"{connection.topic}", f"{connection.msgtype}", message_json])
                except Exception:  # not a valid json, need further inspection
                    self.log.error(f"message_json = {message_json}")
                    raise

                rid = rid + 1
                bytes_wrote = buffer.write(row + '\n')
                size = size + bytes_wrote
                # 50MB chunks max
                if size >= CHUNK_SIZE:
                    yield buffer
                    buffer, size = StringIO(), 0
        # yielding the remaining content.
        yield buffer
