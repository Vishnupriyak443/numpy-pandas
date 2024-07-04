#Abstraction: Create a class called `Animal` with abstract methods like `speak()` and `move()`. 
#Then, create subclasses such as `Dog`, `Cat`, and `Bird` that implement these methods differently.

from abc import ABC,abstractmethod 
class Animal(ABC):
    @abstractmethod
    def speak():
        pass
    def move():
        pass

class Dog(Animal):
    def speak(self):
        print("Dog -Bow Bow")
    def move(self):
        print("Dogs Move with legs")    

class Cat(Animal):
    def speak(self):
        print("Cat-Meow Meow")
    def move(self):
        print("Cats move with legs")    

class Bird(Animal):
    def speak(self):
        print("Bird-koo koo")
    def move(self):
        print("Birds fly")

bird1=Bird()
bird1.speak()
bird1.move()