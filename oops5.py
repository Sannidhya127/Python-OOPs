# we will learn about Class Methods In Python today
class Employee:
    leaves = 9

    def __init__(self, name, salary, office):
        self.name = name
        self.salary = salary
        self.office = office
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    def printdetails(self):
        return f"The name is {self.name}.\nHis salary is {self.salary} and \nHis office is located at {self.office}"

    @classmethod
    def LeaveChanger(cls, newLeaves):
        cls.leaves = newLeaves

    @classmethod
    def from_slash(cls, string):
        # param = string.split("-")
        # print(param)
        # return cls(param[0], param[1], param[2])
        return cls(*string.split("/"))


# I added DDR4 ram today!!!
Harry = Employee("Haris Ali Khan", 1000000, "21/4 Baker street, London")
Rohan = Employee("Rohan Das", 25000, "14 no. Alu Basti, Southern Jupiter")
Karan = Employee.from_slash("Karan Pagla/2345678/Mewari House, Kolkata")
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# print(Harry.printdetails())
# Karan.from_str()
print(Karan.printdetails)
# Harry.LeaveChanger(75678)
# print(Employee.leaves)
# Harry.LeaveChanger(87)
