class Account:
    def __init__(self, name, balance, min_balance,):
        self.years = year
        self.name = name
        self.balance = balance*self.years 
        self.min_balance = min_balance

        
    def deposit(self, amount):
        self.balance +=  amount

    def withdraw(self, amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
        else:
            print("Sorry, not enough funds!")

    def statement(self):
        print("Account Balance: £{}".format(self.balance))

    def years_past(self, year):
        self.years = self.years = input("the number years past: ")

class Current(Account):
    def __init__(self, name, balance, year):
        super().__init__(year, name, balance, min_balance = -1000 )

    def __str__(self):
        return "{}'s Current Account :  £{}".format(self.name, self.balance)

class Savings(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance = 0)

    def __str__(self):
        return "{}'s Savings Account : Balance £{}".format(self.name, self.balance)

    
