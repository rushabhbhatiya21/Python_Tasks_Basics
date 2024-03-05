a = int(input("Please enter a number: "))
b = int(input("Please enter a number: "))
c = int(input("Please enter a number: "))

maxEle, minEle = a, a

if b > maxEle:
    maxEle = b
elif b < minEle:
    minEle = b

if c > maxEle:
    maxEle = c
elif c < minEle:
    minEle = c

print(f'Maximum number is {maxEle} and minimum number is {minEle}')

