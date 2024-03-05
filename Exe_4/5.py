#  5. Using range get me a list of even numbers between 1 and 100. Code needs to be
# done in one line only

print(list(filter(lambda x: x % 2 == 0, range(1, 101))))
