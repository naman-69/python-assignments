
with open("f4.txt", "r") as file:

    sentence = file.readline().strip()
    
upper = 0
lower = 0

for char in sentence:

    if char.isupper():
        upper += 1

    elif char.islower():
        lower += 1

print("UPPER: ", upper)
print("LOWER: ", lower)
