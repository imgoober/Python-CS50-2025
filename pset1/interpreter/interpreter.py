user_input = input("Expression: ")
x, y, z = user_input.split(" ")
if y == "+":
    raw_output = float(x) + float(z)

elif y == "-":
    raw_output = float(x) - float(z)

elif y == "*":
    raw_output = float(x) * float(z)

else:
    raw_output = float(x) / float(z)

print(round(raw_output, 1))
