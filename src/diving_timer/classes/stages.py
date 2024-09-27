from time import sleep


class ExerciseStage:
    is_active = False
    is_finished = False
    sec_counter = 0

    def __init__(self, len_sec: int = 1, stage_name:str = "default stage"):
        self.len_sec: int = len_sec
        self.stage_name = stage_name
        # print(type(self.len_sec))
        pass

    def start_stage(self):
        self.is_active = True
        self.say_stage()
        self.print_stage()
        self.start_countdown()

    def start_countdown(self):
        for i in range(self.len_sec, 0, -1):
            if self.is_active is True and self.is_finished is False:
                print(f"{self.stage_name}: seconds left: {i}")
                sleep(1)
            elif self.is_active is False and self.is_finished is False:
                print(f"{self.stage_name}: Paused")
                self.is_active = False
                break
            elif self.is_finished is True:
                print(f"{self.stage_name}: Finished {self.stage_name}.")
                self.is_active = False
                break
        self.is_finished = True
        self.is_active = False

    def say_stage(self):
        pass

    def print_stage(self):
        print(f"Started {self.stage_name} stage. Len: {self.len_sec} sec.")

#
# class ExerciseStageBreathIn(ExerciseStage):
#     def __init__(self, len_sec: int = 1):
#         super().__init__(len_sec=len_sec)
#
#         pass
#
# class ExerciseStageBreathInHold(ExerciseStage):
#     def __init__(self, len_sec: int = 1):
#         super().__init__(len_sec=len_sec)
#
#         pass
#
# class ExerciseStageBreathOut(ExerciseStage):
#     def __init__(self, len_sec: int = 1):
#         super().__init__(len_sec=len_sec)
#         pass
#
# class ExerciseStageBreathOutHold(ExerciseStage):
#     def __init__(self, len_sec: int = 1):
#         super().__init__(len_sec=len_sec)
#
#         pass
#
