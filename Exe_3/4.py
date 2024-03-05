try:
    a = [1, 2]
    print(a[2])
except IndexError:
    print("IndexError")
else:
    print(a[0])
finally:
    print(a)