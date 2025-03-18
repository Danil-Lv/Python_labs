input_data = input().strip()
words = []
current_word = ''
for char in input_data:
    if char == ' ':
        words.append(current_word)
        current_word = ''
    else:
        current_word += char
words.append(current_word)
new_word = ''
for word in words:
    if word:
        new_word += word[-1].upper()
print(new_word)