import random

random_list = [random.randint(1, 100) for _ in range(10)]
a = list(filter(lambda x: x % 2 == 0, random_list))
b = list(filter(lambda x: x % 2 != 0, random_list))
print(a)
print(b)
