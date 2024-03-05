class ParentClass:
    pass


class ChildClass(ParentClass):
    pass


print(issubclass(ParentClass, ChildClass))
print(issubclass(ChildClass, ParentClass))
