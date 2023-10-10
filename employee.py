"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""
from enum import Enum

'''Pay class encaspulates objects which store information of following:
1. Type of Pay (variable pay or fixed pay)
2. If variable, also stores the number of instances. Uf fixed, by default n = -1
3. Rate of pay
'''
class Pay():
    #enums
    FIXED = 1
    VARIABLE = 2
    
    #constructor
    def __init__(self, type, rate, n):
        self.type = type
        self.rate = rate
        if type == Pay.VARIABLE:
            self.n = n

    def get_pay(self):
        if self.type == Pay.VARIABLE:
            return self.n*self.rate
        elif self.type == Pay.FIXED:
            return self.rate
    
    #getters
    def getType(self):
        return self.type
    def getN(self):
        return self.n
    def getRate(self):
        return self.rate
    
class MonthlyPay(Pay):
    def __init__(self, rate):
        super().__init__(Pay.FIXED, rate, 1)
        
    def __str__(self):
        return f"monthly salary of {self.getRate()}"

class ContractPay(Pay):
    def __init__(self, rate, n):
        super().__init__(Pay.VARIABLE, rate, n)
        
    def __str__(self):
        return f"contract of {self.getN()} hours at {self.getRate()}/hour"
    
class ContractCommission(Pay):
    def __init__(self, rate, n):
        super().__init__(Pay.VARIABLE, rate, n)
        
    def __str__(self):
        return f"commission for {self.getN()} contract(s) at {self.getRate()}/contract"
    
class BonusCommission(Pay):
    def __init__(self, rate):
        super().__init__(Pay.FIXED, rate, 1)
        
    def __str__(self):
        return f"bonus commission of {self.getRate()}"
    
class Employee:
    def __init__(self, name, contract, commission):
        self.name = name
        self.contract = contract
        self.commision = commission

    #calculate total pay
    def get_pay(self):
        if self.commision is None:
            return self.contract.get_pay() 
        else:
            return self.contract.get_pay() + self.commision.get_pay()

    #string representation
    def __str__(self):  
        #If does not recieve commision
        if self.commision is None:
            return f"{self.name} works on a {self.contract}. Their total pay is {self.get_pay()}."
        return f"{self.name} works on a {self.contract} and receives a {self.commision}. Their total pay is {self.get_pay()}."
    


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', MonthlyPay(4000),None)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', ContractPay(25,100), None)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', MonthlyPay(3000), ContractCommission(200, 4))
print(renee)
# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', ContractPay(25, 150), ContractCommission(220, 3))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', MonthlyPay(2000), BonusCommission(1500))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', ContractPay(30, 120),BonusCommission(600))
