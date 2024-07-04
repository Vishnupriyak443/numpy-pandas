#Define a property that must have the same value for every class instance (object)
class property:
    x=5
    def __init__(self):
        pass
    def display(self):
        print("X value:",self.x) 
obj=property()
obj.display()
