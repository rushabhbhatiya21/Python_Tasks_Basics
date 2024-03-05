# Error1 - list out of range
try:
    a = [1, 2]
    print(a[2])
except IndexError:
    print("IndexError")

# Error2 - not defined error
try:
    for i in x:
        print(i)
except NameError:
    print("NameError")


# Error3 - attribute error
class Sample:
    def sample_method(self):
        pass


try:
    sample = Sample()
    print(sample.name)
except AttributeError:
    print('AttributeError')

# Error4 - divide by zero error
try:
    print(4 / 0)
except ZeroDivisionError:
    print('ZeroDivisionError')

# Error5 - TypeError
a = "5"
b = 5.5
try:
    print(a + b)
except TypeError:
    print('TypeError')
