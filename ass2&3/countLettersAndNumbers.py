
with open("f4.txt", "r") as file:

    sentence = file.readline().strip()


letter = 0
digit = 0

for char in sentence:

    if char.isalpha():
        letter += 1

    elif char.isdigit():
        digit += 1

print("LETTERS", letter)
print("DIGITS", digit)
