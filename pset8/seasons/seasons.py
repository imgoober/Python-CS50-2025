import inflect
import sys
from datetime import date

def main():
    birthday = input("Date of Birth: ")
    try:
        birthday = find_date(birthday)
    except ValueError:
        sys.exit("Invalid date")
    mins = find_num_mins(birthday)
    print(int_to_words(mins) + " minutes")


def find_date(date_string):
    try:
        year, month, day = map(int, date_string.split("-"))
        return date(year, month, day)
    except Exception:
        raise ValueError("Invalid date format")

def find_num_mins(birthday):
    today = date.today()
    days = (today - birthday).days
    return days * (60 * 24)


def int_to_words(int):
    engine = inflect.engine()
    text = engine.number_to_words(int, andword="")
    return text.capitalize()


if __name__ == "__main__":
    main()

