val = input("Please enter three numbers separated by spaces: ")

numbers = [int(num) for num in val.split()]

a, b, c = numbers[0], numbers[1], numbers[2]

maxEle = numbers[0]
minEle = numbers[0]

if b > maxEle:
    maxEle = b
elif b < minEle:
    minEle = b

if c > maxEle:
    maxEle = c
elif c < minEle:
    minEle = c

print(f'Maximum number is {maxEle} and minimum number is {minEle}')

