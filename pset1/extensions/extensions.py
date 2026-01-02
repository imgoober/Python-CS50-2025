user_input = input("Enter your file: ")
user_input = user_input.lower()


if ".gif" in user_input:
    print("image/gif")

elif ".jpg" in user_input:
    print("image/jpeg")

elif ".jpeg" in user_input:
    print("image/jpeg")

elif ".png" in user_input:
    print("image/png")

elif ".pdf" in user_input:
    print("application/pdf")

elif ".txt" in user_input:
    print("text/plain")

elif ".zip" in user_input:
    print("application/zip")

else:
    print("application/octet-stream")
