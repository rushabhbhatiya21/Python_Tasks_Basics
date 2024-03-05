def multiply_decorator(factor1, factor2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            multiplied_result = result * (factor1 * factor2)
            return multiplied_result

        return wrapper

    return decorator


@multiply_decorator(2, 3)
def my_function(x, y):
    return x + y


result = my_function(4, 5)

print("Result:", result)
