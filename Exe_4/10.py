hexadecimal_number = '10'

binary_representation = bin(int(hexadecimal_number, 16))
decimal_representation = int(hexadecimal_number, 16)
octal_representation = oct(int(hexadecimal_number, 16))

print(f"Hexadecimal: {hexadecimal_number}")
print(f"Binary: {binary_representation}")
print(f"Decimal: {decimal_representation}")
print(f"Octal: {octal_representation}")
