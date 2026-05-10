# ❓ Problem
# Support:
# Credit Card
# UPI
# PayPal

# 🧠 Thinking
# 👉 Same action → pay()
# 👉 Different implementation



# Abstraction Design
from abc import ABC, abstractmethod
class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


# Implementations
class CardPayment(Payment):
    def pay(self, amount):
        return f"Paid {amount} via Card"
    
class UPIPayment(Payment):
    def pay(self, amount):
        return f"Paid {amount} via UPI"
    
# System Layer
class PaymentProcessor:
    def __init__(self, method: Payment):
        self.method = method

    def process(self, amount):
        return self.method.pay(amount)


# Usage
processor = PaymentProcessor(CardPayment())
print(processor.process(100))  # Output: Paid 100 via Card