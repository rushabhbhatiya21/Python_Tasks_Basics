class MinimumLengthException(Exception):
    def __init__(self, length, minimum_length=5):
        self.message = f"List length must be at least {minimum_length}. Current length: {length}"
        super().__init__(self.message)


def process_list(my_list):
    if len(my_list) < 5:
        raise MinimumLengthException(len(my_list))


try:
    my_list = [1, 2, 3]
    process_list(my_list)
except MinimumLengthException as e:
    print(f"Error: {e}")
