class SampleClass:
    def __init__(self, *args):
        self.args = args

    def getParameters(self):
        return [arg for arg in self.args]


sampleClass = SampleClass(1, 2, 5, 8, 9)
print(sampleClass.getParameters())

sampleClass2 = SampleClass(10, "hello", 12.23, 3.14159265358979, False, (3 + 4j))
print(sampleClass2.getParameters())
