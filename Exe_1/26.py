class MyParentClass:
    a, b = 10, 10
    res1, res2 = 0, 0

    def __init__(self, x=None, y=None):
        if x is not None:
            self.x = x
        else:
            self.x = self.a
        if y is not None:
            self.y = y
        else:
            self.y = self.b
        # self.y = y if y is not None else self.y = self.b

    def sumCustom(self):
        self.res1 = self.x + self.y

    def subCustom(self):
        self.res2 = self.x - self.y

    def __repr__(self):
        return f"Sum: {self.res1}\nSub: {self.res2}"

    def __del__(self):
        print(f"Destructor called {__class__}")


class MyChildClass(MyParentClass):
    c = 10

    def __init__(self, z=None):
        super().__init__()
        if z is not None:
            self.z = z
        else:
            self.z = self.c

    def sumCustom(self):
        self.res1 = self.x + self.y + self.z

    def subCustom(self):
        self.res2 = self.x * self.y * self.z

    def __del__(self):
        print(f"Destructor called {__class__}")


sampleParent = MyParentClass(20, 5)
sampleParent.sumCustom()
sampleParent.subCustom()
print(sampleParent)

sampleChild = MyChildClass(5)
sampleChild.sumCustom()
sampleChild.subCustom()
print(sampleChild)

print("Child Destructor called by manually deleting object: ")
del sampleChild

print("Parent destructor will be called automatically when its deleted in the end of execution.")
