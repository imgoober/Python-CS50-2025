import sys
import csv
from tabulate import tabulate

def main():
    check_command_line()
    table = get_table_data(sys.argv[1])
    print(tabulate(table, headers="keys", tablefmt="grid"))

def check_command_line():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")


def get_table_data(filename):
    try:
        with open(filename, "r") as csvfile:
            csv_reader = csv.DictReader(csvfile)
            return list(csv_reader)
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
