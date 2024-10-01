from datetime import datetime
from src.diving_timer import config

from src.diving_timer.classes.json_operator import JsonOperator
from src.diving_timer.classes.loop import Loop

import logging

logger = logging.getLogger(__name__)


class Exercise:
    time_data = datetime.now()

    def __init__(self, *, input_json_file_path: str):

        # self.set_json_data_from_file(filepath=input_json_file_path)

        self.data = JsonOperator.get_dict_from_json_file(filepath=input_json_file_path)

        self.user_id = self.data["userdata"]["user_id"]
        self.username = self.data["userdata"]["username"]
        self.user_country = self.data["userdata"]["user_country"]
        self.user_timezone = self.data["userdata"]["user_timezone"]
        self.user_language = self.data["userdata"]["user_language"]

        self.loops_needed = self.data["exercise_data"]["loops_needed"]
        self.breath_in_len = self.data["exercise_data"]["breath_in_len"]
        self.breath_in_hold_len = self.data["exercise_data"]["breath_in_hold_len"]
        self.breath_out_len = self.data["exercise_data"]["breath_out_len"]
        self.breath_out_hold_len = self.data["exercise_data"]["breath_out_hold_len"]
        self.exercise_length = self.data["exercise_data"]["exercise_length"]
        self.is_started = False
        self.is_finished = False
        self.exercise_start_datetime = None
        self.exercise_end_datetime = None

        self.loops_in_exercise: list[Loop] = self.initialize_loops_in_list()

    def show(self):
        for loop in self.loops_in_exercise:
            print(f"This is {loop.loop_number} loop.")
            loop.show()

    def initialize_loops_in_list(self) -> list:
        loops_in_exercise = [Loop(exercise=self) for _ in range(self.data["exercise_data"]["loops_needed"])]
        return loops_in_exercise

    def start_exercise(self):
        format_str = "%Y-%m-%d %H:%M:%S"
        self.is_started = True
        self.exercise_start_datetime = datetime.now().strftime(format=format_str)
        for loop in self.loops_in_exercise:
            for stage in loop.stages_in_exercise:
                stage.start_stage()
        self.exercise_end_datetime = datetime.now().strftime(format=format_str)

    def check_if_all_stages_is_finished_true(self) -> bool:
        is_finished_checker = list()
        for loop in self.loops_in_exercise:
            for stage in loop.stages_in_exercise:
                if stage.is_finished is True:
                    is_finished_checker.append(True)
                else:
                    is_finished_checker.append(False)
        if all(is_finished_checker):
            self.is_finished = True
            return True
        else:
            return False

    def count_exercise_len(self) -> int:
        length = self.loops_needed * (self.breath_in_len +
                                                    self.breath_in_hold_len +
                                                    self.breath_out_len +
                                                    self.breath_out_hold_len)
        return int(length)

    def create_exercise_json_output_file(self, *, filepath: str = config.JSON_OUTPUT_FILENAME):
        self.prepare_data_dict()
        JsonOperator.write_json(filepath=filepath, py_dict=self.data)

    def prepare_data_dict(self):
        self.exercise_length = self.count_exercise_len()

        self.data["exercise_data"]["is_started"] = self.is_started
        self.data["exercise_data"]["is_finished"] = self.is_finished
        self.data["exercise_data"]["exercise_start_datetime"] = self.exercise_start_datetime
        self.data["exercise_data"]["exercise_end_datetime"] = self.exercise_end_datetime

        self.data["exercise_data"]["exercise_length"] = self.exercise_length
        self.data["exercise_data"]["loops_needed"] = self.loops_needed
        self.data["exercise_data"]["breath_in_len"] = self.breath_in_len
        self.data["exercise_data"]["breath_in_hold_len"] = self.breath_in_hold_len
        self.data["exercise_data"]["breath_out_len"] = self.breath_out_len
        self.data["exercise_data"]["breath_out_hold_len"] = self.breath_out_hold_len

        self.data["userdata"]["user_id"] = self.user_id
        self.data["userdata"]["username"] = self.username
        self.data["userdata"]["user_country"] = self.user_country
        self.data["userdata"]["user_timezone"] = self.user_timezone
        self.data["userdata"]["user_language"] = self.user_language

