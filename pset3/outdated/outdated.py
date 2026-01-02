months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


while True:
    user_input = input("Date: " ).strip()
    try:
        if "/" in user_input:
            split_date = user_input.split("/")
            if 1 <= int(split_date[0]) <= 12 and 1 <= int(split_date[1]) <= 31:
                print(f"{split_date[2]}", end="-")
                print(f"{int(split_date[0]):02}", end="-")
                print(f"{int(split_date[1]):02}")
                break
            else:
                continue

        elif "," in user_input:
            split_date = user_input.split()
            split_date[1] = split_date[1].replace(",", "")
            for i in range(len(months)):
                if months[i] in split_date[0]:
                    if 1 <= int(i+1) <= 12 and 1 <= int(split_date[1]) <= 31:
                        print(f"{split_date[2]}", end="-")
                        print(f"{(i+1):02}", end="-")
                        print(f"{int(split_date[1]):02}")
                        break
            else:
                continue
            break

    except(ValueError, IndexError):
        continue
