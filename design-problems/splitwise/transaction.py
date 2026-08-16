from user import User

class Transaction:
    def __init__(self, from_user: User, to_user: User, amount: float):
        self.from_user = from_user
        self.to_user = to_user
        self.amount = amount
    
    def settle_transaction(self):
        print(f"settling transaction: sending payment of {self.amount} rs. from {self.from_user} to {self.to_user}")
    
    def __repr__(self):
        return f"{self.from_user} -> {self.to_user}, amount: {self.amount}"
