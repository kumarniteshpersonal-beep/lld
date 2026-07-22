from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class UPIPaymentMethod(PaymentMethod):
    def pay(self, amount):
        print(f"Processing UPI payment of {amount}")

class CreditCardPaymentMethod(PaymentMethod):
    def pay(self, amount):
        print(f"Processing credit card payment of {amount}")


# client code
def process_payment(payment_method, amount):
    if payment_method == "UPI":
        payment = UPIPaymentMethod()
    elif payment_method == "CreditCard":
        payment = CreditCardPaymentMethod()
    else:
        raise ValueError("Invalid payment method")
    payment.pay(amount)

process_payment("UPI", 100)
process_payment("CreditCard", 200)

# problems:
# 1. The client code is tightly coupled with the concrete payment method classes (UPIPaymentMethod and CreditCardPaymentMethod). 
# 2. If we want to add a new payment method, we need to modify the client code, which violates the Open/Closed Principle.