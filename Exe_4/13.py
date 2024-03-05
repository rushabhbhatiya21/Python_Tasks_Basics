def generate_key_values():
    for i in range(65, 91):
        yield chr(i), ord(chr(i))

    for i in range(97, 123):
        yield chr(i), ord(chr(i))

    for i in range(48, 58):
        yield chr(i), ord(chr(i))


def generate_dict():
    dictionary = dict()
    list(map(lambda x: dictionary.update({x[0]: x[1]}), generate_key_values()))
    return dictionary


# list(map(lambda x: print(x), generate_key_values()))
d = generate_dict()
print(d)
