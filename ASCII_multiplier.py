#This script multiplies each character's ASCII code in a string by an integer, does a modulus by 256, and returns each letter's multiplied and modulus'd result into a new string.


import questionary

print("Important: questionary must be installed. To do so first type in bash:\n$ pip install questionary")

input_string = questionary.text("Enter a string: ").ask()
multiplier = questionary.text("Enter an integer: ").ask()

if multiplier.isdigit():
    multiplier = int(multiplier)
else:
    print("Error: integer must be an integer")
    quit()

newstring = ""
for letter in input_string:
    newstring = newstring + chr((ord(letter) * multiplier) % 256)

print(newstring)