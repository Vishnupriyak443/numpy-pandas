#Class Variables: Create a class called `Employee` with a class variable `num_employees` 
#to keep track of the total number of employees created. 
#Increment this variable every time a new employee object is created 
class Employee:
        num_employees=0
        def __init__(self,name,salary):
            self.name=name
            self.salary=salary
        def display(self):
            print("Employees List:")
            print(self.name)
            print(self.salary)
            Employee.num_employees+=1
            print("Total Employees:",self.num_employees)

emp1=Employee("Vishnu",25000) 
emp1.display()
emp2=Employee("Priya",20000)
emp2.display()
emp3=Employee("Vasu",30000)
emp3.display()



