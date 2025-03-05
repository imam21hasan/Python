class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name : {self.name}\tAge : {self.age}")


p1 = person("SHAWON", 22)
p1.display()
