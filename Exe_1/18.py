def one_func():
    print("I am one func")


def two_func():
    print("I am two func")
    one_func()


two_func()
