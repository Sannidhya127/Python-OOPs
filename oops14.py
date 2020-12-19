# This video was for the explanation of Abstraction and Encapsulations in python
import time


class Employee:
    leaves = 9

    def __init__(self, name, salary, office):
        self.name = name
        self.salary = salary
        self.office = office
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    def printdetails(self):
        return f"The name is {self.name}.\nHis salary is {self.salary} and\nHis office is located at {self.office}\nFor repr method output(intended for developers only) call the repr function"

    @classmethod
    def LeaveChanger(cls, newLeaves):
        cls.leaves = newLeaves

    @classmethod
    def from_slash(cls, string):
        # param = string.split("-")
        # print(param)
        # return cls(param[0], param[1], param[2])
        return cls(*string.split("/"))

    def __add__(self, other):
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __repr__(self):
        return f"Employee ({self.name}, {self.salary}, {self.office})\nTo get better output write 'name'.printdetails()\n"

    def __str__(self):
        return self.printdetails()

    @staticmethod
    def printGood(string):
        print("This is a good " + string)
        return ""
        # the return statement returns NULL


        # I added DDR4 ram today!!!
Harry = Employee("Haris Ali Khan", "545",
                 "21/4 Baker street, London")
Rohan = Employee("Rohan Das", 4, "14 no. Alu Basti, Southern Jupiter")
Karan = Employee.from_slash("Karan Pagla/2345678/Mewari House, Kolkata")
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# print(Harry.printdetails())
# Karan.from_str()
# print(Karan.office)
# Harry.LeaveChanger(75678)
# print(Employee.leaves)
# print(Karan.printGood("Harry Kha"))
print(Harry)
