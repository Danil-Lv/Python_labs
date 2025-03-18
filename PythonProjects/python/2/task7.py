input_data = input().strip()
s = ''
i = ''
comma_found = False
for char in input_data:
    if char == ',':
        comma_found = True
    elif not comma_found:
        s += char
    else:
        i += char
count = 0
for char in s:
    if char == i:
        count += 1
    else:
        break
print(count)