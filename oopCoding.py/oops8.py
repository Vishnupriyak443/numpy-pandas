class Employee:
    num_employees=0
    def display(self):
        Employee.num_employees+=1
        print(f"Ttotal Employees:{Employee.num_employees}")


emp1=Employee()
emp1.display()
emp2=Employee()
emp2.display()
