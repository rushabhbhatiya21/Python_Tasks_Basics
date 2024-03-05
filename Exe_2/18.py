my_string = "Python123"

# String validation methods
is_alpha = my_string.isalpha()  # Check if all characters are alphabetic
is_digit = my_string.isdigit()  # Check if all characters are digits
is_alnum = my_string.isalnum()  # Check if all characters are alphanumeric (letters or numbers)
is_upper = my_string.isupper()  # Check if all characters are uppercase
is_lower = my_string.islower()  # Check if all characters are lowercase
is_title = my_string.istitle()  # Check if the string is title cased (first character of each word is uppercase)
is_space = my_string.isspace()  # Check if all characters are whitespaces
is_numeric = my_string.isnumeric()  # Check if all characters are numeric

print(f"Original String: {my_string}")
print(f"isalpha(): {is_alpha}")
print(f"isdigit(): {is_digit}")
print(f"isalnum(): {is_alnum}")
print(f"isupper(): {is_upper}")
print(f"islower(): {is_lower}")
print(f"istitle(): {is_title}")
print(f"isspace(): {is_space}")
print(f"isnumeric(): {is_numeric}")
