file_path = r'f1.txt'
with open(file_path, 'r') as file:
    content = file.read()
    
numbers = content.split(',')
reversed_numbers = ','.join(reversed(numbers))

with open(file_path, 'w') as file:
    file.write(reversed_numbers)

print(f"Contents of {file_path} have been reversed.")
