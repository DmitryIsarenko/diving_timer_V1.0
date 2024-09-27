# from src.logger import setup_logger
from classes.exercice import Exercice

def main():
    ex = Exercice(
        loops_needed=1,
        breath_in_len=1,
        breath_in_hold_len=1,
        breath_out_len=1,
        breath_out_hold_len=1,
        )
    # logger.info("instance of Exercise created")
    ex.show()
    # logger.info("Starting exercise")
    ex.start_exercise()
    ex.form_exercise_data_json()


if __name__ == "__main__":
    # logger = setup_logger(name=__name__, log_file=f"../logs/log.log")
    import src.diving_timer.classes.json_operator
    # main()
