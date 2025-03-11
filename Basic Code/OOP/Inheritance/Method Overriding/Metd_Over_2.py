class car:
    def __init__(self):
        print("This is from super class")

class BMW(car):
    def __init__(self):
        super().__init__()
        print("This is from child class")

c=BMW()