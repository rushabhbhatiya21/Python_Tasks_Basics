# 6. Generate a list of exponents of first 25 integers. Code needs to be in one line only

# print(list(map(lambda x: x ** 2, list(range(1, 26)))))

print(list(map(lambda x: list(map(lambda exp: x ** exp, list(range(1, 5)))), range(1, 26))))
