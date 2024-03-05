class SumCustom:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def doSum(self, op):
        if op:
            return self.a + self.b
        else:
            return self.a, self.b

    def printResults(self):
        print(self.doSum(True))


s = SumCustom(10, 20)
s.printResults()
