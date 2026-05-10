# ✅ STEP 1: Identify Core Actions
# 👉 System does:
# Make payment



# ✅ STEP 2: Identify Variations
# 👉 What changes?
# Card
# UPI
# PayPal




# ✅ STEP 3: Create Abstraction (Contract)
from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass



# ✅ STEP 4: Implement Variations
class CardPayment(Payment):
    def pay(self, amount):
        return f"Paid {amount} via Card"
class UPIPayment(Payment):
    def pay(self, amount):
        return f"Paid {amount} via UPI"
    

    
# ✅ STEP 5: System Class
class PaymentProcessor:
    def __init__(self, payment_method: Payment):      
        self.payment_method = payment_method

    def process(self, amount):
        return self.payment_method.pay(amount)
    



# ✅ STEP 6: Execution
processor = PaymentProcessor(CardPayment())
print(processor.process(100))