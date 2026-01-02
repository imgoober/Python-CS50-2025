import re
import sys


def main():
    print(convert(input("Hours: ")))

def convert(s):
    pattern = r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$"

    match = re.search(pattern, s)
    if not match:
        raise ValueError
    (
        start_hour,
        start_minute,
        start_period,
        end_hour,
        end_minute,
        end_period,
    ) = match.groups()
    start_minute = start_minute or "00"
    end_minute = end_minute or "00"

    start_hour = int(start_hour)
    start_minute = int(start_minute)
    end_hour = int(end_hour)
    end_minute = int(end_minute)
    if not (1 <= start_hour <= 12 and 0 <= start_minute <= 59):
        raise ValueError
    if not (1 <= end_hour <= 12 and 0 <= end_minute <= 59):
        raise ValueError

    if start_period == "AM":
        if start_hour == 12:
            start_hour = 0
    else:
        if start_hour != 12:
            start_hour += 12
    if end_period == "AM":
        if end_hour == 12:
            end_hour = 0
    else:
        if end_hour != 12:
            end_hour += 12

    start_24 = f"{start_hour:02}:{start_minute:02}"
    end_24 = f"{end_hour:02}:{end_minute:02}"

    return f"{start_24} to {end_24}"

if __name__ == "__main__":
    main()
