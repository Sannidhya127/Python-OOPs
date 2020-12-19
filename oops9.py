# we will learn about multilevel inheritance in python today
class Dad:
    basketball = 1


class Son(Dad):
    dance = 1

    def IsDance(self):
        return f"Yes I dance {self.dance} no of times"


class Grandson(Son):
    dance = 6

    def IsDance(self):
        return f"Yes I dance very incredebly {self.dance} no of times"


Harry = Dad()
Marry = Son()
Barry = Grandson()

print(Barry.IsDance())
