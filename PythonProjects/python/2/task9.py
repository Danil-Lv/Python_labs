input_data = input().strip()
cleaned_number = ''
for char in input_data:
    if char in '+0123456789':
        cleaned_number += char
print(cleaned_number)