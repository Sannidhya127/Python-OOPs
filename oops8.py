# we will learn about single inheritence in python today
class Employee:
    leaves = 9
    var = 6

    def __init__(self, name, salary, office):
        self.name = name
        self.salary = salary
        self.office = office
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    def printdetails(self):
        return f"The name is {self.name}.\nHis salary is Rs. {self.salary} and \nHis office is located at {self.office}"

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


class Player:
    no_of_game = 5
    var = 10

    def __init__(self, name, game):
        self.name = name
        self.game = game

    def printPlayerDetails(self):
        return f"The name is {self.name}.\nHis game(s) are {self.game}"


class SuperProgrammer(Employee, Player):
    var = 8


Harry = Employee("Haris Ali Khan", 1000000, "21/4 Baker street, London")
Rohan = Employee("Rohan Das", 25000, "14 no. Alu Basti, Southern Jupiter")
Karan = Employee.from_slash("Karan Pagla/2345678/Mewari House, Kolkata")
Shubham = Player("Shubham Roy", "Cricket, Football,Tennis")
Rajesh = SuperProgrammer("Rajesh Khanna", 109874, "jharudar lane., GopalPur")
Mithilesh = SuperProgrammer(
    "Mithilesh Patnaik", 10, "567 pagla insaan lane, Pagla country, Gadha continent, Mad planet")
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
print(Mithilesh.printdetails())
