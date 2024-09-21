import copy
from time import sleep

from config import (
    exercise_settings,
    EXERCISE_STAGES
    )

loops = copy.deepcopy(exercise_settings["loops"])
breath_in_len = copy.deepcopy(exercise_settings["breath_in_len"])
breath_in_hold = copy.deepcopy(exercise_settings["breath_in_hold"])
breath_out_len = copy.deepcopy(exercise_settings["breath_out_len"])
breath_out_hold = copy.deepcopy(exercise_settings["breath_out_hold"])

total_exercise_time = loops * (
        breath_in_len +
        breath_in_hold +
        breath_out_len +
        breath_out_hold
)


def loop():
    current_loop = 0
    current_stage = 0
    br_in = breath_in_len
    br_hol_in = breath_in_hold
    br_out = breath_out_len
    br_hol_out = breath_out_hold

    while current_loop < loops:
        current_loop += 1

        for current_stage in range(4):
            time_left_on_stage =
            while time_left_on_stage != 0:
                print(f"Exercising: current loop: {current_loop}/{loops}, stage: {EXERCISE_STAGES[current_stage]},"
                      f"time: {time_left_on_stage}")
                sleep(1)
                time_left_on_stage -= 1

        current_stage = 0
        time_left_on_stage = breath_in_len
        while time_left_on_stage != 0:
            print(f"Exercising: current loop: {current_loop}/{loops}, stage: {EXERCISE_STAGES[current_stage]},"
                  f"time: {time_left_on_stage}")
            sleep(1)
            time_left_on_stage -= 1

        current_stage = 1
        time_left_on_stage = breath_in_hold
        while time_left_on_stage != 0:
            print(f"Exercising: current loop: {current_loop}/{loops}, stage: {EXERCISE_STAGES[current_stage]},"
                  f"time: {time_left_on_stage}")
            sleep(1)
            time_left_on_stage -= 1

        current_stage = 2
        time_left_on_stage = breath_out_len
        while time_left_on_stage != 0:
            print(f"Exercising: current loop: {current_loop}/{loops}, stage: {EXERCISE_STAGES[current_stage]},"
                  f"time: {time_left_on_stage}")
            sleep(1)
            time_left_on_stage -= 1

        current_stage = 3
        time_left_on_stage = breath_out_hold
        while time_left_on_stage != 0:
            print(f"Exercising: current loop: {current_loop}/{loops}, stage: {EXERCISE_STAGES[current_stage]},"
                  f"time: {time_left_on_stage}")
            sleep(1)
            time_left_on_stage -= 1


def main():
    pass


if __name__ == "__main__":
    main()
