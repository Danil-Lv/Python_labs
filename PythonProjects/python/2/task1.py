input_data = input()

a, b = input_data.split(',')
a = int(a.strip())
b = int(b.strip())

remainder = a % b

print(remainder)
