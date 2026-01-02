import random

while True:
    try:
        level = input("Level: ")
        if int(level) > 0:
            break
    except ValueError:
        pass

correct_option = random.randint(1, int(level))

while True:
    try:
        user_guess = input("Guess: ")
        if int(level) > 0:
            if int(user_guess) > correct_option:
                print("Too large!")
                pass
            elif int(user_guess) < correct_option:
                print("Too small!")
                pass
            else:
                print("Just right!")
                break
    except ValueError:
        pass


