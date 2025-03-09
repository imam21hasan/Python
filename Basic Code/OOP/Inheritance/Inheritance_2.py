class shape:
    def __init__(self,h,w):
        self.h=h
        self.w=w
    
    def area(self):
        print("This is from shape class")

class triangle(shape):
    def area(self):
        area=.5*self.h*self.w
        print("Area of triangle : ",area)

class rectangle(shape):
    def area(self):
        area=self.h*self.w
        print("Area of rectangle : ",area)

t=triangle(10,20)
t.area()

r=rectangle(10,20)
r.area()