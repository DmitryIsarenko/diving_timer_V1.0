from src.diving_timer.classes.stages import ExerciseStage

class Loop:
    loop_counter = 0

    def __init__(self, exercise):
        Loop.loop_counter += 1
        self.exercise = exercise
        self.loop_number = Loop.loop_counter



        self.stages_in_exercise = self.initialize_stages_in_list()


    def show(self):
        print(
            f"Breath In len: {self.br_in_obj.len_sec}"
            f"Breath In Hold len: {self.br_in_hold_obj.len_sec}"
            f"Breath Out len: {self.br_out_obj.len_sec}"
            f"Breath Out Hold len: {type(self.br_out_hold_obj.len_sec)}"
            # f"Breath Out Hold len: {self.br_out_hold_obj.len_sec}"
            )

    def initialize_stages_in_list(self) -> list:
        br_in_obj = ExerciseStage(len_sec=self.exercise.breath_in_len)
        br_in_hold_obj = ExerciseStage(len_sec=self.exercise.breath_in_hold_len)
        br_out_obj = ExerciseStage(len_sec=self.exercise.breath_out_len)
        br_out_hold_obj = ExerciseStage(len_sec=self.exercise.breath_out_hold_len)
        stages_in_list = [
            br_in_obj,
            br_in_hold_obj,
            br_out_obj,
            br_out_hold_obj,
            ]
        return stages_in_list