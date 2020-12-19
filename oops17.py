import time
import inspect


class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{self.fname}{self.lname}@paglapeople.com"

    def printdetails(self):
        return f"First name is {self.fname}.\nLast name is {self.lname} and email is {self.Email}"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    def __str__(self):
        return self.printdetails()

    @property
    def Email(self):
        if self.fname == None or self.lname == None:
            return f"User has not set any email. Please set it using settter methods made by us"
        else:
            return f"{self.fname}.{self.lname}@codewithharry.com"

    @Email.setter
    def Email(self, string):
        print("Setter method running........")
        time.sleep(2)
        name = string.split("@")[0]
        # print(name)
        self.fname = name.split(".")[0]
        self.lname = name.split(".")[1]

    @Email.deleter
    def Email(self):
        self.fname = None
        self.lname = None


SkillF = Employee("Skill", "F")
Rony = Employee("Rony", "Debnath")
o = "This is a string"
# print(Rony.Email)
# print(inspect.getmembers(SkillF))
print(SkillF)
