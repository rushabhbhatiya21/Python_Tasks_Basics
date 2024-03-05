def func(a, b, c=-1, d=-1, e=-1):
    if c == -1 and d == -1 and e == -1:
        return a * b
    elif d == -1 and e == -1:
        return a, b, c
    elif e == -1:
        return a + b + c + d
    else:
        return (a * b) + (c * d * e)


print(func(10, 20))
print(func(10, 20, 30))
print(func(10, 20, 30, 40))
print(func(10, 20, 30, 40, 50))
