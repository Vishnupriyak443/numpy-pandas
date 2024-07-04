#Composition: Create a class called `Book` with attributes like `title`, `author`, and `publisher`. 
#Then, create a class called `Library` that contains a collection of `Book` objects.
class Book:
    def __init__(self,title,author,publisher):
        self.title=title
        self.author=author
        self.publisher=publisher
    
class Library():
    
    def __init__(self):
        self.list=[]
    def append(self):
        #option-2 
        #def append(self,title,author,publisher):
        self.b1=Book( "ABC","Mr.X","XYZ Publisers")  
       #self.b2=Book(title,author,publisher)
        self.list.append(self.b1)
    def display(self):    
        for i in self.list:
            print(f"Title:{self.b1.title}")
            print(f"Author:{self.b1.author}")
            print(f"Publisher:{self.b1.publisher}")


obj1=Library()
obj1.append()
obj1.display()
#option-2
#obj2=Library()
#obj2.append("ABC","Mr.x","111 Publishers")
#obj2.display()

