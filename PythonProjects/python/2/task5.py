domain = input().strip()
parts = []
current_part = ""
for char in domain:
    if char == '.':
        parts.append(current_part)
        current_part = ""
    else:
        current_part += char
parts.append(current_part)
for part in reversed(parts):
    print(part)