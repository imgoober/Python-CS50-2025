def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if (2 <= len(s) <= 6) is False:
        return False

    if s[0:2].isalpha() is False:
        return False

    if not s.isalnum():
        return False

    for i in range(len(s)):
        if s[i].isdigit():
            if not s[i:].isdigit():
               return False
            if s[i] == "0":
                if s[:i].isalpha():
                    return False

    return True

if __name__ == "__main__":
    main()
