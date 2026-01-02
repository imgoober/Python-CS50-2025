user_input = input("camelCase: ")

print("SnakeCase: ", end = "")

for i in user_input:
    if i.isupper():
        print("_" + i.lower(), end = "")
    else:
        print(i, end = "")

print("\n", end = "")
