import sys
import random
from pyfiglet import Figlet
figlet = Figlet()

fonts = figlet.getFonts()

if len(sys.argv) < 3:
    print("Invalid usage")
    sys.exit(1)
if sys.argv[1] != "-f" and sys.argv[1] != "--font":
    print("Invalid usage")
    sys.exit(1)

try:
    if sys.argv[2] not in fonts:
            sys.exit(1)

except IndexError:
    print("Invalid usage")


f = sys.argv[2]
user_input = input("Input: ")

figlet.setFont(font=f)
print(figlet.renderText(user_input))
