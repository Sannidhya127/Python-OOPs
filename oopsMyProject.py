class School_Employees:
    position = "Teacher"
    salary = 25000
    pass


Roshan = School_Employees()  # Principal
Albert = School_Employees()
Harry = School_Employees()  # Moderator
Rohan = School_Employees()
Shubham = School_Employees()
Raju = School_Employees()  # Chief Teacher
Ranchor = School_Employees()
Phunsukh = School_Employees()
Chatur = School_Employees()  # Chief Clarke
Farahn = School_Employees()  # Vice Principal
Post = School_Employees()
Rohan.name = "Rohan Das"
Rohan.tclass = 8, 9, 6
Rohan.age = 36

principal_step = ("Student in St. Xavier's School Kolkata. " "Teacher in the same school from 1990. " "Asst. Teacher from 1996 to 2001",
                  "Senior Teacher in 2002", "Vice Principal from 2003 to 2008", "Principal since 2009")

Roshan.name = "Roshan Singh Harjit Singh Sodhi"
Roshan.tclass = 12
Roshan.age = 56
Roshan.position = "Principal"
Roshan.salary = 60000
Roshan.steps = principal_step


Harry.name = "Haris Ali Khan"
Harry.tclass = 11, 12
Harry.age = 43

Raju.name = "Raju Rastogi"
Raju.tclass = 11, 12, 10, 7, 8
Raju.position = "Chief Teacher"
Raju.salary = 45000
Raju.age = 39

Farahn.name = "Farahn Quereshi"
Farahn.age = 80

Chatur.name = "Chatur Lal"
Chatur.age = 26

Albert.name = "Albert Ekka"
Albert.tclass = 3, 2, 4
Albert.age = 30

Shubham.name = "Shubham Roy"
Shubham.tclass = 12, 11, 9
Shubham.age = 36

Ranchor.name = "Ranchor Das Shyamal Das Chanchar"
Ranchor.tclass = 6, 7, 5
Ranchor.age = 27

Phunsukh.name = "Phunsukh Wangdu"
Phunsukh.tclass = 11, 10
Phunsukh.age = 45


Post.principal = Roshan.name
Post.vice_principal = "Farahn Quereshi"
Post.chief_teacher = "Raju Rastogi"
Post.chief_clarke = Chatur.name

# /// ********* Weight: Weight is the force by which a body is attracted towards the center of the earth.**********\\\


print(Roshan.steps)
# print(Roshan.position)
# print(Ranchor.name)
# print(Raju.position)
# print(Post.chief_clarke)
# print(Post.principal)
# print(Chatur.__dict__)
# print(Farahn.__dict__)
