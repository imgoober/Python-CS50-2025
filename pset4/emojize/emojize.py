import emoji

user_input = input("Input: ")
print("Output: ", end="")
print(emoji.emojize(user_input, language='alias'))
