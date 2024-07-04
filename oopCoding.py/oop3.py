#Encapsulation: 
#Create a class called `BankAccount` that encapsulates the account balance. 
#Include methods to deposit money, withdraw money, and display the current balance.
class BankAccount:
    def __init__( self):
        self.__acc_bal=0  #private
    def deposit(self,dep_money):
        self.deposit=dep_money
    def withdraw(self,withdraw_money):
        self.withdraw=withdraw_money   
    def display(self):    
        self.__acc_bal=self.deposit-self.withdraw
        print("Account balance:",self.__acc_bal)

acc1=BankAccount()
acc1.deposit(1000)
acc1.withdraw(200)
acc1.display()
