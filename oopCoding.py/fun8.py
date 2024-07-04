#Write a Python program to create a Vehicle class with max_speed and mileage instance attributes
class vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed=max_speed
        self.mileage=mileage
    def display(self):
        print(self.max_speed) 
        print(self.mileage)
v1=vehicle(100,60)
v1.display()   
       