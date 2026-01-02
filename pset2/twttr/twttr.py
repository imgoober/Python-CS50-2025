vowels = ['A', 'a', "E", 'e', "I", 'i', "O", 'o', "U", 'u']

user_input = input("Input: ")

print("Output: ", end = "")

for i in user_input:
    if i in vowels:
        print("", end = "")
    else:
        print(i, end = "")

print("")




