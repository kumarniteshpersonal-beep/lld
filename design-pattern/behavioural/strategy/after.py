from abc import ABC, abstractmethod

# strategy interface
class PaymentProcessorStrategy(ABC):
    @abstractmethod
    def process_payment(self, amount: float):
        pass

class AmazonWalletPaymentProcessor(PaymentProcessorStrategy):
    def process_payment(self, amount: float):
        print(f"Processing payment of {amount} through Amazon Wallet")

class CreditCardPaymentProcessor(PaymentProcessorStrategy):
    def process_payment(self, amount: float):
        print(f"Processing payment of {amount} through Credit Card")

# context class
class PaymentContext:
    def __init__(self, strategy: PaymentProcessorStrategy):
        self.strategy = strategy
    
    def set_strategy(self, strategy: PaymentProcessorStrategy):
        self.strategy = strategy
    
    def execute_payment(self, amount: float):
        self.strategy.process_payment(amount)

# client code
payment_context = PaymentContext(AmazonWalletPaymentProcessor())
payment_context.execute_payment(100)

payment_context.set_strategy(CreditCardPaymentProcessor())
payment_context.execute_payment(200)
