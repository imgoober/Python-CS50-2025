import sys

def main():
    check_command_line()
    try:
        file_path = sys.argv[1]
        with open(file_path, "r") as file:
            loc_count = 0
            for line in file:
                if check_line(line):
                    loc_count +=1
            print(loc_count)
    except FileNotFoundError:
        sys.exit("File does not exist")


def check_command_line():
    if len(sys.argv) < 2:
        sys.exit("Too many command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")


def check_line(line):
    if line.isspace():
        return False
    if line.lstrip().startswith("#"):
        return False
    return True



if __name__ == "__main__":
    main()
