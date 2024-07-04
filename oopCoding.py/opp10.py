#Error Handling: Create a class called `Calculator` with methods like `add()`, `subtract()`, `multiply()`, and `divide()`. 
#Implement error handling to catch exceptions like division by zero or invalid input
class Calculator:
    
    def add(self,x,y):
        self.x=x
        self.y=y
        print(f"Addition :{self.x+self.y}")
    def subtract(self,x,y):
        self.x=x
        self.y=y
        print(f"Subtraction :{self.x-self.y}")   
    def multiply(self,x,y):
        self.x=x
        self.y=y
        print(f"Multiplication :{self.x*self.y}")
    def divide(self,x,y): 
        try:
            self.x=x
            self.y=y
            print("Division :",self.x/self.y) 
        except:
            print("Error:zero division error")
obj=Calculator()
obj.divide(123,0)



    

