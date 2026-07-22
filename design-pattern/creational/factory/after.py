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

class PaymentFactory:
    @staticmethod
    def create_payment_method(payment_method: str) -> PaymentMethod:
        if payment_method == "UPI":
            return UPIPaymentMethod()
        elif payment_method == "CreditCard":
            return CreditCardPaymentMethod()
        else:
            raise ValueError("Invalid payment method")

# client code
def process_payment(payment_method, amount):
    payment = PaymentFactory.create_payment_method(payment_method)
    payment.pay(amount)

process_payment("UPI", 100)
process_payment("CreditCard", 200)

# core component:
# 1. Factory Class: This class is responsible for creating instances of payment methods based on the type.
# 2. Interface / Abstract class: Interface for concrete class
# 3. Concrete Class: These are the actual implementations of the payment methods (UPIPaymentMethod and CreditCardPaymentMethod).