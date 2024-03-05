# 8. Create a generator method which gives random numbers between 1 and 100 and
# the number not being repeated. Make sure it generates only 10 numbers.
from random import random, randint


def get_random_number(random_numbers):
    while True:
        number = randint(1, 101)
        if number not in random_numbers:
            return number


def generate_random_unique_numbers():
    random_numbers = set()
    for i in range(10):
        number = get_random_number(random_numbers)
        random_numbers.add(number)
        yield number


list(map(lambda x: print(x), generate_random_unique_numbers()))
