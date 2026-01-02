def value(greeting):

    spaceless_greeting = greeting.lower().strip()

    if "hello" in spaceless_greeting:
        return "$0"

    elif "h" in spaceless_greeting[0]:
        return "$20"

    else:
        return "$100"
