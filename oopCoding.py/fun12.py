#Create a Bus child class that inherits from the Vehicle class. 
#The default fare charge of any vehicle is seating capacity * 100. 
#If Bus is Vehicle instance, we need to add an extra 10% on full fare as a maintenance charge.
#So total fare for bus instance will become the final amount = total fare + 10% of the total fare 
class Vehicle:
    def total_Charge(self,seat_cap):
        self.seat_cap=seat_cap
        
class Bus(Vehicle):
    def charge( self,seat_cap):
        tot_Fare=seat_cap*100
        return tot_Fare    
v1=Bus( )
full_Fare= v1.charge(15)
print(full_Fare)
    