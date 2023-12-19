from pathlib import Path
from rosbags.highlevel import AnyReader
from pathlib import Path
from rosbags.typesys import get_types_from_msg, register_types
from rosbags.serde import deserialize_cdr
from os import walk
from collections.abc import MutableMapping
import logging

class Parser():
    def __init__(self, custom_message_path=""):
        logging.basicConfig(
            level=logging.DEBUG,
            format='[%(asctime)s.%(msecs)03d][%(funcName)s][%(levelname)s] %(message)s',
            datefmt='%H:%M:%S'
        )

        self.log = logging.getLogger('Uploader')
        self.log.setLevel(logging.DEBUG)
        self.nested_dict_type = "rosbags.usertypes"
        if len(custom_message_path) > 0:
            for msg in custom_message_path:
                self.register_custom_messages(msg)

    def guess_msgtype(self, path: Path) -> str:
        """Guess message type name from path."""
        name = path.relative_to(path.parents[2]).with_suffix('')
        if 'msg' not in name.parts:
            name = name.parent / 'msg' / name.name
        return str(name)

    def register_custom_messages(self, message_folder_path):
        add_types = {}

        msgs = [next(walk(message_folder_path), (None, None, []))[2]][0]

        for pathstr in msgs:
            msgpath = Path(message_folder_path + pathstr)
            msgdef = msgpath.read_text(encoding='utf-8')
            add_types.update(get_types_from_msg(
                msgdef, self.guess_msgtype(msgpath)))
            self.log.debug(f"adding {msgpath} as custom message")

        register_types(add_types)

    def flatten_dict(self, dictionary: dict, parent_key: str='', separator: str='.') -> dict:
        items = []
        for key, value in dictionary.items():
            new_key = parent_key + separator + key if parent_key else key
            try:
                if "/msg/" in value.__msgtype__:
                    value = self.deserialized_message_to_dict(value)
                    items.extend(self.flatten_dict(
                        value, new_key, separator=separator).items())
            except:
                items.append((new_key, value))
        return dict(items)
    
    def nest_dict(self, flat_dict):
        nested_dict = {}
        
        for key, value in flat_dict.items():
            keys = key.split(".")
            d = nested_dict
            for k in keys[:-1]:
                d = d.setdefault(k, {})
            d[keys[-1]] = value
            
        return nested_dict

    def deserialized_message_to_dict(self, dictionary: dict) -> dict:
        items = {}
        if type(dictionary) != "dict":
            dictionary = dictionary.__dict__
        for key, value in dictionary.items():
            value_type = str(type(value))
            if self.nested_dict_type in value_type:
                items[key] = self.deserialized_message_to_dict(value)
            else:
                items[key] = value
        return dict(items)
