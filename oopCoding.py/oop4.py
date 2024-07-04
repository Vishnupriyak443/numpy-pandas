#Polymorphism: Create a class called `Shape` with a method `area()`. 
#Then, create subclasses such as `Rectangle`, `Circle`, and `Triangle` 
#that override the `area()` method to calculate the area specific to each shape.
class Shape():
    def area():
        pass

class Rectangle(Shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        print("Area of a Rectangle:",self.l*self.b)    
class Circle(Shape):
    pi=3.14
    def __init__(self,r):
        self.r=r
    def area(self):
        print("Area of the circle:",self.pi*self.r**2)
class Triangle(Shape):
    def __init__(self,b,h):
        self.base=b
        self.height=h
    def area(self):
        print("Area of the triangle:",self.base*self.height/2)
obj=Rectangle(10,20)
obj.area()
obj=Circle(3)
obj.area()
obj=Triangle(3,5)
obj.area()


