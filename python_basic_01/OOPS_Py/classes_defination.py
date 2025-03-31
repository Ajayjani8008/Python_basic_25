class Car:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
        
    def car_full_name(self):
        return f"{self.brand} {self.model}"
    
class Electric_car(Car):
    def __init__(self,battery_size,brand,model,year):
        super().__init__(brand,model,year)
        self.battery_size=battery_size
        
new_electric_car = Electric_car(100,"Tesla","Model 3",2022)

print("Full Name:", new_electric_car.car_full_name())
print("Brand:", new_electric_car.brand)
print("Model:", new_electric_car.model)    
print("Year:", new_electric_car.year)
print("Battery Size:", new_electric_car.battery_size)
        
my_car = Car("Toyota", "Camry", 2022)

print("Full Name:", my_car.car_full_name())
print("Brand:", my_car.brand)
print("Model:", my_car.model)    
print("Year:", my_car.year)
    