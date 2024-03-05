a = [1, 2, 3, 4, 5, 6, 7, 8]
b = [4, 5, 6, 7, 8, 9, 10]


def findCommonElements(a, b):
    return [i for i in a if i in b]


print(findCommonElements(a, b))
