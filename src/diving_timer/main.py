# from pprint import pprint
from src.diving_timer import config
from src.diving_timer.classes.exercise import Exercise

import logging

logger = logging.getLogger("src")


def main():
    ex = Exercise(input_json_file_path=config.JSON_INPUT_FILEPATH)

    logger.info("instance of Exercise created")
    ex.show()
    logger.info("Starting exercise")

    ex.start_exercise()
    ex.create_exercise_json_output_file(filepath=config.JSON_OUTPUT_FILENAME)


if __name__ == "__main__":
    main()
