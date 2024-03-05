import random


def add_random_values(func):
    def wrapper(*args, **kwargs):
        random_value1 = random.randint(1, 10)
        random_value2 = random.randint(1, 10)

        result = func(*args, **kwargs, random_value1=random_value1, random_value2=random_value2)

        print(f"Random Values: {random_value1}, {random_value2}")

        return result

    return wrapper


@add_random_values
def add(random_value1, random_value2):
    return random_value1 + random_value2


@add_random_values
def sub(random_value1, random_value2):
    return random_value1 - random_value2


@add_random_values
def mul(random_value1, random_value2):
    return random_value1 * random_value2


@add_random_values
def div(random_value1, random_value2):
    return random_value1 / random_value2


result_add = add()
result_sub = sub()
result_mul = mul()
result_div = div()

print(f"Addition Result: {result_add}")
print(f"Subtraction Result: {result_sub}")
print(f"Multiplication Result: {result_mul}")
print(f"Division Result: {result_div}")
