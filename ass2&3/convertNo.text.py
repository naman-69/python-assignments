
def number_to_text(num):
    
    num_dict = {
        0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
        6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
        11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
        15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
        19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty',
        50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'
    }

    if 0 <= num <= 20:
        return num_dict[num]
    elif 21 <= num <= 99:
        tens = num // 10 * 10
        ones = num % 10
        return num_dict[tens] + ('' if ones == 0 else '-' + num_dict[ones])
    elif 100 <= num <= 999:
        hundreds = num // 100
        remainder = num % 100
        return num_dict[hundreds] + ' hundred' + ('' if remainder == 0 else ' and ' + number_to_text(remainder))
    else:
        return "Number out of range"

file_path = r'D:\Python\python Lab\1\f2.txt'

with open(file_path, 'r') as file:
   
    content = file.read()

words = content.split()

converted_words = [number_to_text(int(word)) if word.isdigit() else word for word in words]


converted_content = ' '.join(converted_words)

with open(file_path, 'w') as file:
    # Write the converted content back to the file
    file.write(converted_content)
print("numbers in f2.txt has been converted to text");