import random


def main():
    level = get_level()
    generate_integer
    incorrect = 0
    for i in range(10):
        errors = 0
        first_integer = generate_integer(level)
        second_integer = generate_integer(level)

        while True:
            try:
                print(f"{first_integer} + {second_integer} =", end = "")
                user_input = input()
                if int(user_input) == (first_integer + second_integer):
                    break
                else:
                    print("EEE")
                    errors = errors + 1
            except ValueError:
                errors = errors + 1
                print("EEE")


            if errors == 3:
                incorrect = incorrect + 1
                print(f"{first_integer} + {second_integer} = {first_integer} + {second_integer}")
                print(first_integer + second_integer)
                break

    score = 10 - incorrect
    print(f"Score: {score}")




def get_level():
    while True:
        try:
            level = input("Level: ")
            if int(level) > 0 and int(level) <= 3:
                return int(level)
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
