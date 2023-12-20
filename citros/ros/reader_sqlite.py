from io import StringIO
import traceback
import datetime 
import sqlite3
import json
import os


CHUNK_SIZE = 50 * 1024 * 1024

###############
##### PG ######
############### 
class BagReaderSQL():
    def read_messages(self, input_bag, simulation_run_id):
        print(" + read_messages:")
        from rosidl_runtime_py.convert import get_message_slot_types, message_to_yaml, message_to_csv, message_to_ordereddict
        from rosidl_runtime_py.utilities import get_message
        from rclpy.serialization import deserialize_message
        
        self.conn = sqlite3.connect(input_bag)
        self.cursor = self.conn.cursor()

        topics_data = self.cursor.execute("SELECT id, name, type FROM topics").fetchall()
        self.topics = {name_of:{'type':type_of, 'id':id_of, 'message':get_message(type_of) } for id_of,name_of,type_of in topics_data}
        
        buffer = StringIO()
        size = 0
        for topic_name in self.topics.keys():
            if topic_name in ["/rosout", "/client_count", "/connected_clients"]:
                continue
            rows = self.cursor.execute(f"select id, timestamp, data from messages where topic_id = {self.topics[topic_name]['id']}").fetchall()            
            rid = 0
            for id, timestamp, data in rows:
                d_data = deserialize_message(data, self.topics[topic_name]["message"])
                msg_dict = message_to_ordereddict(d_data)
                json_data = json.dumps(msg_dict)
                
                row = chr(0x1E).join([f"{simulation_run_id}", f"{rid}", f"{timestamp}", f"{topic_name}", f"{self.topics[topic_name]['type']}", json_data])
                rid = rid + 1
                bytes_wrote = buffer.write(row + '\n')
                size = size + bytes_wrote
                # 10MB chunks max
                if size >= CHUNK_SIZE:                    
                    yield buffer
                    buffer, size = StringIO(), 0
        # return the rest of the file.
        yield buffer
