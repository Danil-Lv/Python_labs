def decimal_to_binary(n):
    if n == 0:
        return "0"
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary

def decimal_to_octal(n):
    if n == 0:
        return "0"
    octal = ""
    while n > 0:
        octal = str(n % 8) + octal
        n = n // 8
    return octal

def decimal_to_hex(n):
    if n == 0:
        return "0"
    hex_digits = "0123456789ABCDEF"
    hex_num = ""
    while n > 0:
        hex_num = hex_digits[n % 16] + hex_num
        n = n // 16
    return hex_num

input_data = input().strip()
if not input_data.isdigit() or int(input_data) <= 0:
    print("Неверный ввод")
else:
    num = int(input_data)
    binary = decimal_to_binary(num)
    octal = decimal_to_octal(num)
    hex_num = decimal_to_hex(num)
    print(f"{binary}, {octal}, {hex_num}")