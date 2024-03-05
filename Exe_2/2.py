def getEvenElements():
    elements = [i for i in range(1, 21)]
    return [i for i in elements if i % 2 == 0]


print(getEvenElements())
