class PaymentProcessor:
    def process_payment(self, payment_type: str, amount: float):
        if payment_type == "amazon_wallet":
            print(f"Processing payment of {amount} through Amazon Wallet")
        elif payment_type == "credit_card":
            print(f"Processing payment of {amount} through Credit Card")
        else:
            raise ValueError(f"Unsupported payment type: {payment_type}")

processor = PaymentProcessor()
processor.process_payment("amazon_wallet", 100)
processor.process_payment("credit_card", 200)