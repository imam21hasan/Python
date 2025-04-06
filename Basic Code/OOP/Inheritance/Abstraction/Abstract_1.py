from abc import ABC, abstractmethod

class shape(ABC):
    def __init__(self, h, w):
        self.h = h
        self.w = w

    @abstractmethod
    def area(self):
        pass


class triangle(shape):
    def area(self):
        area = .5*self.h*self.w
        print("Area of triangle : ", area)


class rectangle(shape):
    def area(self):
        area = self.h*self.w
        print("Area of rectangle : ", area)


t = triangle(12, 20)
t.area()

r = rectangle(15, 20)
r.area()
