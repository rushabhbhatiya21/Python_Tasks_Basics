s1, s2, s3 = "hello", "Hello", "HellO"


def checkIsTitle(s) -> bool:
    return s.istitle()


print(list(map(checkIsTitle, [s1, s2, s3])))
print(list(filter(checkIsTitle, [s1, s2, s3])))
        