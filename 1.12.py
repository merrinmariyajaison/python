class Account:
    def __init__(self,ano,name,balance=0):
        self.ano=ano
        self.name=name
        self.balance=balance
    def display(self):
        print(f"Balance :{self.balance}\n")
class Deposit(Account):
    def __init__(self,ano,name,balance=0):
        super().__init__(ano,name,balance)
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}\nNew balance is {self.balance}.")
        else:
            print("Invalid deposit amount.")
class Withdraw(Account):
    def __init__(self,ano,name,balance=0):
        super().__init__(ano,name,balance)
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Invalid or insufficient funds for withdrawal.")
account = Account("123456", "ABC", 1000)
account.display()

deposit_acc = Deposit("123456", "ABC", account.balance)
deposit_acc.deposit(500)
deposit_acc.display()

withdraw_acc = Withdraw("123456", "ABC", deposit_acc.balance)
withdraw_acc.withdraw(200)
withdraw_acc.display()

