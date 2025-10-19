class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def info(self):
        return f"{self.make} {self.model}"

car = Car("Toyota", "Corolla")
print(car.info())
