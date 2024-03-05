class ParentClass:
    def common_method(self):
        print("This is a common method in the parent class")


class ChildClass(ParentClass):
    def common_method(self):
        print("This is the overridden method in the child class")


parent_obj = ParentClass()

parent_obj.common_method()

print("\n")

child_obj = ChildClass()

child_obj.common_method()
