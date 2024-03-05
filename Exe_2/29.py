a = list(range(1, 11))
b = list(range(11, 21))


def add(a, b):
    return a + b


c = list(map(lambda x, y: x + y, a, b))
print(c)
