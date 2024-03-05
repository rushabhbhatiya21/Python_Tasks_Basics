# Multiple Inheritance
class P1:
    def method1(self):
        print("This is P1.method1")


class P2:
    def method2(self):
        print("This is P2.method2")


class C1(P1, P2):
    def method3(self):
        print("This is C1")


print("Multiple Inheritance Example: ")
c1 = C1()

c1.method1()
c1.method2()
c1.method3()


# Multi level Inheritance

class GrandParent:
    def grandParentMethod(self):
        print("This is GrandParentMethod")


class Parent(GrandParent):
    def parentMethod(self):
        print("This is parentMethod")


class Child(Parent):
    def childMethod(self):
        print("This is childMethod")


print("Multi-Level Inheritance Example: ")

parent = Parent()
parent.grandParentMethod()
parent.parentMethod()

child = Child()
child.grandParentMethod()
child.parentMethod()
child.childMethod()
