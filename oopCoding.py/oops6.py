class Book:
    def __init__(self,title,author,publisher):
        self.title=title
        self.author=author
        self.publisher=publisher
    def __str__(self):
        return f"{self.title}:{self.author}:{self.publisher}"
     
    
class Library():
    
    def __init__(self,b_name):
        self.b_name=b_name
        self.list=[]
    def append(self,title,author,publisher):
        self.b=Book( title,author,publisher)  
        self.list.append(self.b)
    def display(self):    
        print(f"Book name:{self.b_name}")
        for i in self.list:
            print(self.b)


obj1=Library("Book1")
obj1.append("ABC","Mr.X","XYZ Publishers")
obj1.display()
obj2=Library("Book2")
obj2.append("abc","Mr.x","123 Publishers")
obj2.display()

