class ParentClass:
    def __init__(self):
        print("Parent object created")
    def parent_method1(self):
        print("This is parent method 1")

    def parent_method2(self):
        print("This is parent method 2")

    def __del__(self):
        print("Parent object deleted")

class ChildClass(ParentClass):
    def __init__(self):
        super().__init__()
        print("Child object created")
    def child_method(self):
        print("This is child method")

    def __del__(self):
        print("Child object deleted")


parent_obj = ParentClass()

parent_obj.parent_method1()
parent_obj.parent_method2()

print("\n")

child_obj = ChildClass()

child_obj.parent_method1()
child_obj.parent_method2()
child_obj.child_method()
