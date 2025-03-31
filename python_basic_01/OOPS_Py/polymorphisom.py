class Car:
    def __init__(self,brand,model,year):
        self.__brand=brand
        self.model=model
        self.year=year
        
    def car_full_name(self):
        return f"{self.__brand} {self.model}"
    
    def get_brand(self):
        return self.__brand + "__from getter__"
    
    def fuel_type(self):
        return "Petrol or diesel"
    
class Electric_car(Car):
    def __init__(self,battery_size,brand,model,year):
        super().__init__(brand,model,year)
        self.battery_size=battery_size
    def fuel_type(self):
        return "Eletric charge"        

new_car = Car("Toyota", "Camry", 2022)
new_electric_car = Electric_car(100,"Tesla","Model 3",2022)
print(new_electric_car.get_brand())

print(new_electric_car.fuel_type())
print(new_car.fuel_type())
    

