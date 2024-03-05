octal_number = '13'

binary_representation = bin(int(octal_number, 8))
decimal_representation = int(octal_number, 8)
hexadecimal_representation = hex(int(octal_number, 8))

print(f"Octal: {octal_number}")
print(f"Binary: {binary_representation}")
print(f"Decimal: {decimal_representation}")
print(f"Hexadecimal: {hexadecimal_representation}")
