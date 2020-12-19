from abc import ABCMeta, abstractmethod
# from abc import ABC, abstractmethod


class Shape(metaclass=ABCMeta):
    @abstractmethod
    def Area(self):
        return 0


class rectangle(Shape):
    type = "Rectangle"
    sides = 4

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def Area(self):
        return self.length * self.breadth


rec1 = rectangle(5, 3)
# print(rec1.Area())

print(147-63)
