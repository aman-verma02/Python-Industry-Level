# Custom Exceptions

class PaymentError(Exception):
    pass

class InsufficientFundsError(PaymentError):
    pass

class PaymentGatewayError(PaymentError):
    pass



# Implementation

class PaymentService:

    def pay(self, amount, balance):
        if balance < amount:
            raise InsufficientFundsError("Not enough balance")

        if amount > 10000:
            raise PaymentGatewayError("Gateway limit exceeded")

        return "Payment successful"
    

# Usage

try:
    service = PaymentService()
    service.pay(15000, 20000)

except InsufficientFundsError:
    print("User needs to recharge")

except PaymentGatewayError:
    print("Try smaller amount")

except PaymentError:
    print("Something went wrong")