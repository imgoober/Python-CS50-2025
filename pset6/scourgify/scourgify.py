import sys
import csv

def main():
    check_command_line()
    data = load_data(sys.argv[1])
    save(sys.argv[2], data)


def check_command_line():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")


def load_data(filename):
    students = []
    try:
        with open(filename) as file:
            reader = csv.DictReader(file)
            for student in reader:
                last, first = student["name"].split(", ")
                student = {"first": first, "last": last, "house": student["house"]}
                students.append(student)
        return students
    except FileNotFoundError:
        sys.exit(f"Could not read {filename}")


def save(filename, data):
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames = ["first", "last", "house"])
        writer.writeheader()
        writer.writerows(data)


if __name__ == "__main__":
    main()
