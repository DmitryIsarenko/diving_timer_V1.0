import json
import os
import logging

logger = logging.getLogger(__name__)

logger.debug("Msg from JSON package")
logger.info("Msg from JSON package")
logger.warning("Msg from JSON package")
logger.error("Msg from JSON package")
logger.critical("Msg from JSON package")


class JsonOperator:
    def __init__(self):
        pass

    def find_json(self, *, filepath: str) -> list[json]:
        files_list = os.listdir()
        for file in files_list:
            if type(file) is json:
                pass
        return []

    def read_json(self, *, filepath: str) -> dict:
        pass

    def write_json(self, *, filepath: str) -> bool:
        pass

    def send_json_to_db(self, *, filepath: str, db) -> bool:
        pass

    def get_json_from_db(self, *, filepath: str, db) -> bool:
        pass
