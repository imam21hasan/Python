class Parent1:
    def method1(self):
        print("From Parent1")


class Parent2:
    def method2(self):
        print("From Parent2")


class Child(Parent1, Parent2):
    def method3(self):
        print("From Child")


obj = Child()
obj.method1()
obj.method2()
obj.method3()
