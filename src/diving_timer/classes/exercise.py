from datetime import datetime
from pickletools import pydict

from src.diving_timer.classes.json_operator import JsonOperator
from src.diving_timer.classes.loop import Loop

import logging

logger = logging.getLogger(__name__)


class Exercise:
    time_data = datetime.now()
    is_started = False
    is_interrupted = False
    is_finished = False

    def __init__(
            self, *,
            loops_needed: int = 1,
            breath_in_len: int = 1,
            breath_in_hold_len: int = 1,
            breath_out_len: int = 1,
            breath_out_hold_len: int = 1,
            ):

        res = self.set_json_data_from_file()
        if res:
            logger.info(f"Set data from a file.")
        else:
            self.loops_needed = loops_needed
            self.breath_in_len = breath_in_len
            self.breath_in_hold_len = breath_in_hold_len
            self.breath_out_len = breath_out_len
            self.breath_out_hold_len = breath_out_hold_len
            logger.info(f"Set data from an input.")


        self.exercise_data = {
            "loops_needed": self.loops_needed,
            "breath_in_len": self.breath_in_len,
            "breath_in_hold_len": self.breath_in_hold_len,
            "breath_out_len": self.breath_out_len,
            "breath_out_hold_len": self.breath_out_hold_len,
            }

        self.loops_in_exercise: list[Loop] = self.initialize_loops_in_list()

    def show(self):
        for loop in self.loops_in_exercise:
            print(f"This is {loop.loop_number} loop.")
            loop.show()

    def initialize_loops_in_list(self) -> list:
        loops_in_exercise = [Loop(exercise=self) for _ in range(self.loops_needed)]
        return loops_in_exercise

    def start_exercise(self):
        for loop in self.loops_in_exercise:
            for stage in loop.stages_in_exercise:
                stage.start_stage()

    def check_if_all_stages_is_finished_true(self):
        is_finished = list()
        for loop in self.loops_in_exercise:
            for stage in loop.stages_in_exercise:
                if stage.is_finished is True:
                    is_finished.append(True)
                else:
                    is_finished.append(False)
        if all(is_finished):
            return True
        else:
            return False

    def form_exercise_data_json(self):
        is_exercise_finished = self.check_if_all_stages_is_finished_true()
        if is_exercise_finished:
            logger.info("Exercise finished, making json")
        JsonOperator.write_json(filepath="../jsondata.json",py_dict=self.exercise_data)


    def set_json_data_from_file(self) -> bool:
        files = JsonOperator.get_json_files_from_dir(filepath="../")
        if files:
            pydict = JsonOperator.read_json(filepath=f"../{files[0]}")

            self.loops_needed = pydict["loops_needed"]
            self.breath_in_len = pydict["breath_in_len"]
            self.breath_in_hold_len = pydict["breath_in_hold_len"]
            self.breath_out_len = pydict["breath_out_len"]
            self.breath_out_hold_len = pydict["breath_out_hold_len"]
            return True
        else:
            return False