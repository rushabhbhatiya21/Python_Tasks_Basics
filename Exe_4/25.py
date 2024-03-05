import random

random_list = [random.randint(1, 100) for _ in range(10)]
print(random_list)
print(''.join(map(str, random_list)))

