def square_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result ** 2

    return wrapper


def increase_by_10_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + 10

    return wrapper


@increase_by_10_decorator
@square_decorator
def my_function(x):
    return x


result = my_function(10)

# Printing the result
print("Result:", result)
