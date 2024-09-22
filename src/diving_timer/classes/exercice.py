from datetime import datetime


class Exercice:
    time_data = datetime.now()
    is_started = False
    is_interrupted = False
    is_finished = False
    def __init__(self,
                 loops: int = 1,
                 breath_in_len: int = 1,
                 breath_in_hold: int = 1,
                 breath_out_len: int = 1,
                 breath_out_hold: int = 1,
                 ):
        self.loops = loops
        self.breath_in_len = breath_in_len
        self.breath_in_hold = breath_in_hold
        self.breath_out_len = breath_out_len
        self.breath_out_hold = breath_out_hold

