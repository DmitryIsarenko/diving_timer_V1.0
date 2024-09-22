class ExerciseStage:
    is_active = False
    sec_counter = 0
    def __init__(self, len_sec: int = 1):
        self.len_sec: int = len_sec
        print(type(self.len_sec))
        pass
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
