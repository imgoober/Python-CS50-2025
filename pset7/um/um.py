import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    matches = re.findall(r"\bum\b", s, re.IGNORECASE) # looks confusing since there aren't seperators but \b is a word boundary
    # IGNORECASE also makes it so that um, uM, Um, and UM all work

    return len(matches)


if __name__ == "__main__":
    main()
