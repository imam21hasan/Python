class grandfather:
    def display1(self):
        print("This is from Grandfather")


class father(grandfather):
    def display2(self):
        print("This is from Father")


class child(father):
    def display3(self):
        super().display1()
        super().display2()
        print("This is from Child")


c = child()
c.display3()
