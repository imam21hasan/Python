class car:
    def display(self):
        print("This is from Car\n")


class bike:
    def display(self):
        print("This is from Bike")


class vehicle1(car,bike):
    pass

class vehicle2(bike,car):
    pass

v1 = vehicle1()
v1.display()

v2=vehicle2()
v2.display()
