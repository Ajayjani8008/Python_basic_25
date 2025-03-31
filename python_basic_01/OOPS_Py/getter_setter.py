class Car:
    total_car = 0
    def __init__(self, brand, model, year):
        self.__brand = brand
        self.model = model
        self.year = year
        Car.total_car += 1

    def car_full_name(self):
        return f"{self.__brand} {self.model}"

    def get_brand(self):
        return self.__brand + "__from getter__"


class Electric_car(Car):
    def __init__(self, battery_size, brand, model, year):
        super().__init__(brand, model, year)
        self.battery_size = battery_size



new_electric_car = Electric_car(100, "Tesla", "Model 3", 2022)
new_electric_car2 = Electric_car(100, "Tesla", "Model 3", 2022)
new_car = Car("Toyota", "Camry", 2022)


print(new_electric_car.get_brand())
print(Car.total_car)
