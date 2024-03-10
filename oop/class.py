class car:
    def __init__(self, make, model , year):
        self.make = make
        self.model = model
        self.year = year
        
    def display_car_details(self):
        print(f"Car: {self.make} {self.model} {self.year}")
        
my_car = car("Toyota", "Corolla ", 2020)

my_car.display_car_details()