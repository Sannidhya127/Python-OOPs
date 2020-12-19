# ////////////////////// // Diamond Shape problem in python\\\\\\\\\\\\\\\\\\\\\\\\\\\

# for d.met it first checks for the function in class D. If not in class D then in order of class D(B, C) it first checks Class B then Class C. If it gets a met function in Class B it prints it without moving further but in case it doesn't get it moves to class C. If it doesn't get it in class C also then lastly it checks class A or the parent of all. If not getting even there it shows an error


class A:
    def met(self):
        print("This is a method from class A")


class B(A):
    def met(self):
        print("This is a method from class B")


class C(A):
    def met(self):
        print("This is a method from class C")


class D(B, C):
    def met(self):
        print("This is a method from class D")


a = A()
b = B()
c = C()
d = D()

d.met()
