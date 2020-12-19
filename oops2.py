# we will learn more on instancces and class here:


class Employee:
    leaves = 9
    pass


Harry = Employee()
Rohan = Employee()
Bhargav = Employee()


# print(Harry.leaves)
Employee.leaves = 23

Rohan.office = "14 no. Alu Basti, Southern Jupiter"
Bhargav.name = "bhargav monkey"
Bhargav.salary = 1000
Bhargav.office = "Unknown"
Harry.name = "Haris Ali Khan"
Harry.salary = 1000000
Harry.office = "21/4 Baker street, London"
Rohan.name = "Rohan Singh"
Rohan.salary = 25000
# print(Harry.leaves)
Harry.leaves = 89
# print(Harry.leaves)
# print(Harry.__dict__)
# print(Rohan.office)
print(Bhargav.name)
