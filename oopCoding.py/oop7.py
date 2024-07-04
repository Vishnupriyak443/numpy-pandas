#Method Overriding: Create a base class called `Employee` with a method `calculate_salary()`. 
#Then, create subclasses such as `Manager` and `Developer` that override the `calculate_salary()` method based on their roles.
class Employee():
    def calculate_salary(self):
        self.basic=20000
        self.allowances=5000
        self.deductions=3000
        self.salary=self.basic+self.allowances-self.deductions
        print("Salary of an employee:",self.salary)

class Manager(Employee):
    Employee.calculate_salary(self=Employee)
    def calculate_salary(self):
        self.basic=35000
        self.allowances=5000
        self.deductions=4000
        self.salary=self.basic+self.allowances-self.deductions
        print("Salary of a manager:",self.salary)

class Developer(Employee):
    def calculate_salary(self):
        self.basic=35000
        self.allowances=6000
        self.deductions=5000
        self.salary=self.basic+self.allowances-self.deductions
        print("Salary of a Developer:",self.salary)

mg1=Manager( )
mg1.calculate_salary()
dev1=Developer()
dev1.calculate_salary()
