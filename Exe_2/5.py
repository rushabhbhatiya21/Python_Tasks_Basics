x, y = (1, 2, 3, 4, 5), (4, 5, 6, 7)

c = tuple(filter(lambda elem: elem not in x or elem not in y, x + y))
print(c)
