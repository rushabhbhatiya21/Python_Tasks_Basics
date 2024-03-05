binary_number = '11010001111100111'

decimal_representation = int(binary_number, 2)
hexadecimal_representation = hex(int(binary_number, 2))
octal_representation = oct(int(binary_number, 2))

print(f"Binary: {binary_number}")
print(f"Decimal: {decimal_representation}")
print(f"Hexadecimal: {hexadecimal_representation}")
print(f"Octal: {octal_representation}")
