# Encapsulation is the process of hiding the internal details of an object and only exposing a public interface. This is achieved by using access modifiers (like private, protected, and public) to restrict access to certain parts of the code. In reality, it’s about control, safety, and system integrity. By encapsulating data and behavior, we can prevent unauthorized access and modification, which helps to maintain the integrity of the system. It also allows us to change the internal implementation without affecting the external code that relies on it, making our code more flexible and easier to maintain.


class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private     we use double underscore to make the variable private, which means it cannot be accessed directly from outside the class. In this way __balance can only be accessed and modified through the methods provided by the class, ensuring that the integrity of the data is maintained.                                                                                              acc = BankAccount(1000) acc.balance = -5000   # ❌ invalid state

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance
    


class BankAccount:
    def __init__(self):
        self.__balance = 1000   # private

    def __show_balance(self):   # private method
        return self.__balance
    

acc = BankAccount()

print(acc.__balance)   # ❌ ERROR

print(acc._BankAccount__balance)   # ✅ Accessing private variable using name mangling