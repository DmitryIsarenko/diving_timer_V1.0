from classes.exercice import Exercice


def main():
    ex = Exercice(
        loops_needed=1,
        breath_in_len=1,
        breath_in_hold_len=1,
        breath_out_len=1,
        breath_out_hold_len=1,
        )
    ex.show()
    ex.start_exercise()
    ex.form_exercise_data_json()


if __name__ == "__main__":
    main()
