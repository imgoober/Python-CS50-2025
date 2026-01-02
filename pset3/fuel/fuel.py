def main():
    fraction = input("Fraction: ")
    percent = convert(fraction)
    print(gauge(percent))

def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)
    if x<0 or x>y:
        raise ValueError
    return round((x/y)*100)


def gauge(percent):
    if percent <= 1:
        return "E"
    elif percent >= 99:
        return "F"
    else:
        return f"{percent}%"

if __name__ == "__main__":
    main()

