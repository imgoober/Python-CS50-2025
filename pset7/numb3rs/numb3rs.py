import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    ip_sections = ip.split(".")
    if len(ip_sections) != 4:
        return False
    for section in ip_sections:
        if not section.isdigit():
            return False
        if section[0] == "0" and len(section) > 1:
            return False
        try:
            if not 0 <= int(section) <= 255:
                return False
        except ValueError:
            return False
    return True

if __name__ == "__main__":
    main()
