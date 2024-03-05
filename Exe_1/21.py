class ParentClass:
    def parent_method1(self):
        print("This is parent method 1")

    def parent_method2(self):
        print("This is parent method 2")


class ChildClass(ParentClass):
    def child_method(self):
        print("This is child method")


parent_obj = ParentClass()

parent_obj.parent_method1()
parent_obj.parent_method2()

print("\n")

child_obj = ChildClass()

child_obj.parent_method1()
child_obj.parent_method2()
child_obj.child_method()
