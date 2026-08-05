from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        pass

class CreditCardPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> bool:
        # Implement credit card payment processing logic here
        print(f"Processing credit card payment of ${amount:.2f}")
        return True  # Simulate successful payment

class WalletPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> bool:
        # Implement Wallet payment processing logic here
        print(f"Processing Wallet payment of ${amount:.2f}")
        return True  # Simulate successful payment