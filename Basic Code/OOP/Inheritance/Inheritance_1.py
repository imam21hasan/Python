class car:
    def model(self):
        print("Model : xxxxx")

    def speed(self):
        print("Top speed 325 kmh")


class BMW(car):
    def name(self):
        print("This is BMW")


c = BMW()
c.name()
c.model()
c.speed()
