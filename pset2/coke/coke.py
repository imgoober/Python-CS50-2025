cents_due = 50

while cents_due > 0:
    print("Amount due:", cents_due)
    user_input = int(input("Insert coin: "))

    #cents_due = cents_due - user_input

    if user_input in [25, 10, 5]:
        cents_due = cents_due - user_input

change_due = abs(cents_due)
print("Change Owed:", change_due )

