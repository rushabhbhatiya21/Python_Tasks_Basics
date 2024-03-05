class CustomDictClass:
    def __init__(self, d):
        self.d = d

    def printDict(self):
        for key, value in self.d.items():
            if key is not None:
                print(f'{key}: {value}')


# d1 = CustomDictClass(dict.fromkeys(range(1, 11), 1))
# d1.printDict()
