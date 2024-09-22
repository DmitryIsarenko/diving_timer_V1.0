from datetime import datetime
from src.diving_timer.classes.loop import Loop
from src.diving_timer.classes.stages import (
    ExerciseStage,
    # ExerciseStageBreathIn,
    # ExerciseStageBreathInHold,
    # ExerciseStageBreathOut,
    # ExerciseStageBreathOutHold
    )


class Exercice:
    time_data = datetime.now()
    is_started = False
    is_interrupted = False
    is_finished = False

    # loops: int = 1
    # breath_in_len: int = 5,
    # breath_in_hold_len: int = 10,
    # breath_out_len: int = 7,
    # breath_out_hold_len: int = 11,

    def __init__(
            self, *, loops_needed: int = 1,
            breath_in_len: int = 1,
            breath_in_hold_len: int = 1,
            breath_out_len: int = 1,
            breath_out_hold_len: int = 1,
            ):
        self.loops_needed = loops_needed
        self.breath_in_len = breath_in_len
        self.breath_in_hold_len = breath_in_hold_len
        self.breath_out_len = breath_out_len
        self.breath_out_hold_len = breath_out_hold_len

        self.loops_in_exercise = self.initialize_loops_in_list()
        print(type(self.loops_in_exercise))

    def show(self):
        for loop in self.loops_in_exercise:
            print(f"This is {loop.loop_number} loop.")
            loop.show()

    def initialize_loops_in_list(self) -> list:
        loops_in_exercise = [Loop(exercise=self) for _ in range(self.loops_needed)]
        return loops_in_exercise

