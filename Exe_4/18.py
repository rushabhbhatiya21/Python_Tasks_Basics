import random

random_list = [random.choice([0, 1]) for _ in range(10)]

if all(element == 1 for element in random_list):
    print("ALL")
elif any(element == 1 for element in random_list):
    print("ANY")
elif all(element == 0 for element in random_list):
    print("NONE")

print("Generated List:", random_list)
