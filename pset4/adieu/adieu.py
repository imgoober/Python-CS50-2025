try:
    names = []
    while True:
        user_input = input("Name: ")
        names.append(user_input)


except EOFError:
    print()
    print("Adieu, adieu, to ", end="")
    if len(names) == 1:
        print(names[0])
    elif len(names) == 2:
        print(names[0] + " and " + names[1])
    else:
        for i in range(len(names) - 1):
            print(names[i], end=", ")
        print("and " + names[-1])







