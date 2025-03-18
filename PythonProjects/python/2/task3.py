input_data = input()
a = ''
b = ''
c = ''
space_count = 0
for char in input_data:
    if char == ' ':
        space_count += 1
    elif space_count == 0:
        a += char
    elif space_count == 1:
        b += char
    elif space_count == 2:
        c += char
a = int(a)
b = int(b)
c = int(c)
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
print(b)