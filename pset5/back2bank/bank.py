def value(greeting):

    spaceless_greeting = greeting.lower().strip()

    if "hello" in spaceless_greeting:
        return 0

    elif spaceless_greeting.startswith("h"):
        return 20

    else:
        return 100
