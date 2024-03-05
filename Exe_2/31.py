l1, l2 = [i for i in range(1, 6)], [i for i in range(4, 8)]

print(list(filter(lambda i: i not in l2 or i not in l1, l1 + l2)))
