def main():
    time = input("What time is it? ")
    numerical_time = convert(time)
    if numerical_time >= 7 and numerical_time <= 8:
        print("breakfast time")
    elif numerical_time >= 12 and numerical_time <= 13:
        print("lunch time")
    elif numerical_time >= 18 and numerical_time <= 19:
        print("dinner time")
    #else:
        #print("")


def convert(time):
    hours, minutes = time.split(":")
    numerical_minutes = float(minutes) / 60
    return float(hours) + numerical_minutes


if __name__ == "__main__":
    main()
