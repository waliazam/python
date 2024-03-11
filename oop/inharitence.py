class Vehicle:  # Parent class
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(f"This is a {self.make} {self.model}.")

class Car(Vehicle):  # Child class inheriting from Vehicle
    def __init__(self, make, model, year):
        super().__init__(make, model)  # Call to the parent class's __init__ method
        self.year = year

    def display_car_details(self):
        print(f"Car: {self.year} {self.make} {self.model}")

# Using the child class
my_car = Car("Toyota", "Corolla", 2020)
my_car.display_info()         # Inherits method from the parent class
my_car.display_car_details()  # Output: Car: 2020 Toyota Corolla
