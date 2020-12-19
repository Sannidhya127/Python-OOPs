import time


class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{self.fname}{self.lname}@paglapeople.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

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


Haris = Employee("Haris", "Khan")
Nikhil = Employee("Nikhil", "Pandey")

print(Haris.Email)
Haris.Email = "James.Bond"
print(Haris.Email)
print(Haris.explain())
# del Haris.Email
print(Haris.Email)
