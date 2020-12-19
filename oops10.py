# we will learn about access modifiers in python today
class Employee:
    leaves = 9  # Public variable
    _protected = "This variable is protected"  # Protected variable
    __private = "This variable is private"  # Private variable

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

    @staticmethod
    def printGood(string):
        print("This is a good " + string)
        return ""
        # the return statement returns NULL

        # I added DDR4 ram today!!!


class Programmer(Employee):
    def __init__(self, name, salary, office, lang, OsPref):
        self.name = name
        self.salary = salary
        self.office = office
        self.lang = lang
        self.OsPref = OsPref

    def printProg(self):
        return f"The name of the programmer is {self.name}.\nHis salary is {self.salary} and \nHis office is located at {self.office}. the languages {self.name} knows are {self.lang} and the OS prefference is {self.OsPref}"


Harry = Employee("Haris Ali Khan", 1000000, "21/4 Baker street, London")
Rohan = Employee("Rohan Das", 25000, "14 no. Alu Basti, Southern Jupiter")
Karan = Employee.from_slash("Karan Pagla/2345678/Mewari House, Kolkata")
Sannidhya = Programmer("Sannidhya Dasgupta", 300235, "Kingston Houses, Rover Road, Switz Hill",
                       "HTML, CSS, JavaScript, PHP, Python\n(including it's libraries), C, C++, Java, GoLang", "Linux")
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
emp = Employee("empty man", 34, "hulo biral road")
print(emp._Employee__private)
