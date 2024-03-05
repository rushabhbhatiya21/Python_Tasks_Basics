print("using while loop: ")
n = 0
while n < 10:
    if n % 2 == 0:
        n += 1
        continue
    print(n)
    n += 1

print("using for loop: ")
for i in range(1,11):
    if i % 2 == 0:
        continue
    print(i)
