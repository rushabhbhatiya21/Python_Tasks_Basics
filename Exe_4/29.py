import random

random_numbers = [random.randint(1, 100) for _ in range(25)]

print("Original List:", random_numbers)

sorted_numbers = sorted(random_numbers)
print("Sorted List:", sorted_numbers)
