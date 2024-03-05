a, b, c = 10, 10, -10

if (a > 0 and b > 0) or (b > 0 and c > 0) or (a > 0 and c > 0):
    print("The numbers are greater than 0")
if a > 0 and b > 0 and c > 0:
    print("All the numbers are greater than 0")
else:
    print("At least one number is not greater than 0")