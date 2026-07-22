from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class UPIPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paying {amount} using UPI")

class CreditCardPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paying {amount} using Credit Card")

def process_payment(payment_method: PaymentMethod, amount):
    payment_method.pay(amount)

# Example usage
process_payment(UPIPayment(), 1000) # Output: Paying 1000 using UPI
process_payment(CreditCardPayment(), 2000) # Output: Paying 2000 using Credit Card
# process_payment(PaymentMethod(), 500) # This will raise an error because PaymentMethod is an abstract class and cannot be instantiated directly.