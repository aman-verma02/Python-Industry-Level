

"""
❓ Problem
Design a BankAccount system with:
deposit(amount)
withdraw(amount)
transfer(other_account, amount)
transaction history
prevent negative balance

🧠 Thinking
You need:
state → balance
list → transaction history
validation → no negative
interaction between objects → transfer

"""

class BankAccount:
    def __init__(self, name, balance=0, ):
        self.name = name
        self.balance = balance
        self.history = []  # store transactions

    def deposit(self, amount):
        if amount <= 0:
            return "Invalid deposit amount"
        
        self.balance += amount
        self.history.append(f"Deposited {amount}")

    def withdraw(self, amount):
        if amount <= 0:
            return "Invalid withdrawal amount"
        
        if amount > self.balance:
            return "Insufficient balance"
        
        self.balance -= amount
        self.history.append(f"Withdrew {amount}")

    def transfer(self, other_account, amount):
        if self.withdraw(amount) == "Insufficient balance":
            return "Transfer failed"
        
        other_account.deposit(amount)
        self.history.append(f"Transferred {amount} to {other_account.name}")

    def show_history(self):
        return self.history

    def check_balance(self):
        return self.balance
    




a1 = BankAccount("Trek", 1000)
a2 = BankAccount("Alex", 500)

a1.deposit(500)
a1.withdraw(200)
a1.transfer(a2, 300)

print(a1.check_balance())
print(a2.check_balance())
print(a1.show_history())