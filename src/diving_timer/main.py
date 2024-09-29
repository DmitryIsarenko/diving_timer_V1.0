# from src.logger import setup_logger
from src.diving_timer.classes.exercise import Exercise


import logging
logger = logging.getLogger(__name__)

def main():
    ex = Exercise(
        loops_needed=0,
        breath_in_len=1,
        breath_in_hold_len=1,
        breath_out_len=1,
        breath_out_hold_len=1,
        )
    logger.info("instance of Exercise created")
    ex.show()
    logger.info("Starting exercise")
    ex.start_exercise()
    ex.form_exercise_data_json()


if __name__ == "__main__":
    main()
