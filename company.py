import time as t


class Company:
    comp_name = "Google"


class Employee(Company):
    posts = ("CEO", 'CTO', "GPU Software developers", "Web Develoipers(Full Stack)", "Web developers(Front End)", "Web Developers(backe End)",
             "Data Scientists(Senior)", "Data Scientists(Junior)", "Machine Learning Engineers", "Artificial Intelligence Developers", "Dev Ops")
    query = input("Please enter your choice:\nP for all posts list\n S for a specific post and see it's details\nEa for adding Employees\nEr for removing emloyees\nChange")

    for i in posts:
        print(i)
