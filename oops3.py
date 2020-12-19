# we will learn about Self & __init__()(Constructors) today
class Employee:
    leaves = 9

    def __init__(self, name, salary, office):
        self.name = name
        self.salary = salary
        self.office = office
# I happy to see no lags of this computer any more :) (:

    def printdeatails(self):
        return f"The name is {self.name}.\nHis salary is {self.salary} and \nHis office is located at {self.office}"


Harry = Employee("Haris Ali Khan", 1000000, "21/4 Baker street, London")
Rohan = Employee("Rohan Das", 25000, "14 no. Alu Basti, Southern Jupiter")
Sannidhya = Employee("Sannidhya Dasupta", 25000000,
                     "21 Rajani Sen Road, Kolkata 700030")
# I just can't take it any more. I feel like dieing. Life is now no less thn hell to me.
# Harry.name = "Haris Ali Khan"
# Harry.salary = 1000000
# Harry.office = "21/4 Baker street, London"
# Rohan.name = "Rohan Singh"
# Rohan.salary = 25000
# Rohan.office = "14 no. Alu Basti, Southern Jupiter"

print(Sannidhya.printdeatails())
# print(Rohan.name)

# This is a python OOPs Code. It is the most important thing in Python. OOPs let's you do that work which if done without OOPs will take you hundreds of lines of code. SO! Learn OOPS properly!!!!!!
