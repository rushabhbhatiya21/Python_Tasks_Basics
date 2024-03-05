#  2. Create an assertion for a string to check the length of the string being minimum of
# 10 letters.

try:
    a = input("Enter a string of minimum length 10: ")
    assert len(a) >= 10
    print(a)
except AssertionError:
    print("Minimum length of string must be greater than or equal to 10")
