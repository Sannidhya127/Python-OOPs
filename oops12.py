class A:
    varclass1 = "I am in class A"

    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.varclass1 = "I am instance variable in class a"


class B(A):
    varclass1 = "I am in class B"

    def __init__(self):
        super().__init__()
        self.var2 = "I am inside class B's constructor"
        self.varclass2 = "I am instance variable in class B"


a = A()
b = B()

print(b.varclass1)
