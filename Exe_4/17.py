class Sample:
    def __init__(self, sample1=0, sample2=0, sample3=0, sample4=0):
        self.sample1 = sample1
        self.sample2 = sample2
        self.sample3 = sample3
        self.sample4 = sample4


sample = Sample()

print(hasattr(sample, 'sample1'))
print(hasattr(sample, 'sample5'))

setattr(sample, 'sample1', 10)
print(getattr(sample, 'sample1'))
print(getattr(sample, 'sample2'))

print(hasattr(sample, 'sample1'))
delattr(sample, 'sample1')
print(hasattr(sample, 'sample1'))
