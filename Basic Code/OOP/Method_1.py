class student:
    name = ""
    roll = ""

    def setValue(self, name, roll):
        self.name = name
        self.roll = roll

    def display(self):
        print(f"Name : {self.name}  Roll : {self.roll}")


s1 = student()
s1.setValue("SHAWON", 1008)
s1.display()