# 4. Using range get me a list of 1 to 10 and from this list generate a list as
# [13,15,17,19,21,23,25,27,29,31]. Code needs to be done in one line only.

print(list(map(lambda x: 12 + (x - 1) + x, list(range(1, 11)))))
