#Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
class Bus(Vehicle):
    def display(self):
        print(self.name)
        print(self.max_speed)
        print(self.mileage)
v1=Bus('Bus',100,120)    
v1.display()    
