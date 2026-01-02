def main():
    user_input = input("Try typing a happy or sad emoticon: ")
    result = convert(user_input)
    print(result)


def convert(user_input):
    msg = user_input.replace(':)', '🙂')
    msg2 = msg.replace(':(', '🙁')
    return msg2

main()
