class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.brand} {self.model}"

car1 = Car("BMW", "i8", 2025)
car2 = Car("Ferrari", "SF90 Spider", 2024)

print(car1.display_info())
print(car2.display_info())
