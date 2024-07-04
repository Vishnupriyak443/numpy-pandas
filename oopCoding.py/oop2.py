#INHERITANCE
class Vehicle:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
class Car(Vehicle):
    def __init__(self,make,model,year,num_doors,fuel_type):
        self.num_doors=num_doors
        self.fuel_type=fuel_type
        super().__init__(make,model,year)
    def display(self):
        print("Make:",self.make)
        print("Model:",self.model)
        print("Year:",self.year)
        print("Number of doors:",self.num_doors)
        print("Fuel type:",self.fuel_type)
obj=Car("Ford","F21",2001,4,"petrol")
obj.display()
