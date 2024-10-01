import json
import os
import logging
from xml.sax import parse

logger = logging.getLogger(__name__)


class JsonOperator:
    def __init__(self):
        pass

    @staticmethod
    def get_json_files_from_dir(*, filepath: str) -> list[json]:
        files = list()
        files_list = os.listdir(path=filepath)
        logger.info(f"list of json files: {files_list}")
        for file in files_list:
            if ".json" in file[-5::]:
                files.append(file)
        return files

    @staticmethod
    def get_dict_from_json_file(*, filepath: str) -> dict:
        with open(file=filepath, mode="r") as file:
            json_str = json.load(fp=file)
            return json_str

    @staticmethod
    def write_json(*, filepath: str, py_dict: dict) -> None:
        with open(file=filepath, mode="w") as file:
            json.dump(obj=py_dict, fp=file, sort_keys=True, indent=4)

    def send_json_to_db(self, *, filepath: str, db) -> bool:
        pass

    def get_json_from_db(self, *, filepath: str, db) -> bool:
        pass
