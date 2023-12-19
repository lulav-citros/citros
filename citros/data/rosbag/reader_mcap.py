from io import StringIO
import traceback
import datetime 
import os

import json
import yaml

class BagReaderMcap():
    def read_messages(self, input_bag, simulation_run_id):             
        from rosidl_runtime_py.convert import get_message_slot_types, message_to_yaml, message_to_csv, message_to_ordereddict
        from rosidl_runtime_py.utilities import get_message
        from rclpy.serialization import deserialize_message
        import rosbag2_py

        reader = rosbag2_py.SequentialReader()
        reader.open(
            rosbag2_py.StorageOptions(uri=input_bag, storage_id="mcap"),
            rosbag2_py.ConverterOptions(
                input_serialization_format="cdr", output_serialization_format="cdr"
            ),
        )

        topic_types = reader.get_all_topics_and_types()

        def typename(topic_name):
            for topic_type in topic_types:
                if topic_type.name == topic_name:
                    return topic_type.type
            raise ValueError(f"topic {topic_name} not in bag")
        
        topic_counters = {}
        buffer = StringIO()    
        
        while reader.has_next():  
                 
            topic, data, timestamp = reader.read_next()
            
            msg_type = get_message(typename(topic))
            
            msg = deserialize_message(data, msg_type)
            
            yaml_msg = message_to_yaml(msg)
            
            data = yaml.load(yaml_msg, Loader=yaml.FullLoader)
            
            json_data = json.dumps(data)
            
            # msg_dict = message_to_ordereddict(msg)
            # print("json:", topic, msg_type, "\n",json_data)            
            
            id = topic_counters.get(topic, -1) + 1
            topic_counters[topic] = id
            # TODO:[ ] return ros message id?
            row = chr(0x1E).join([f"{sid}", f"{id}", f"{timestamp}", f"{topic}", f"{msg_type}", f"{json_data}\n"])            
            buffer.write(row)       
                                
        del reader
        return buffer
