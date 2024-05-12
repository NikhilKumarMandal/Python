class Car:
    total_Car = 0
    def __init__(self,brand,model):
        self.__brand = brand
        self.__model = model
        Car.total_Car += 1
    def fullname(self):
        return f"{self.__brand} {self.__model}"
    def get_brand(self):
        return self.__brand + " !"
    def fuel_type(self):
        return 'Petrol or Diesel'
    @staticmethod
    def genreal_desc():
        return "Car is mine of transport"
    @property
    def model(self):
        return self.__model


class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size 
    def fuel_type(self):
        return 'Electric Charge'


# tesla_Car = ElectricCar("tesla","model S","85kmh")
# print(tesla_Car.brand)
# print(tesla_Car.fuel_type())


# print(isinstance(tesla_Car,Car) )
# print(isinstance(tesla_Car,ElectricCar) )

# my_Car = Car("tata","safari")
# print(my_Car.fuel_type())
# print(Car.genreal_desc())

# print(Car.total_Car)
# print(my_Car.model)
# print(my_Car.brand)
# print(my_Car.fullname())


class Battery:
    def battery_info(self):
        return "This is a battery"


class Engine:
    def engine_info(self):
        return "This is engine"

class ElectricCar2(Battery,Engine,Car):
    pass


my_new_tesla = ElectricCar2("Tesla","model S")
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())