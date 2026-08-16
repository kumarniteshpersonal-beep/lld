from collections import defaultdict
from user import User

class BalanceSheet:
    def __init__(self, owner: User):
        # map<other_user: balance>
        # self -> other_user and balance is amount which self has to give to other user
        self.balance = defaultdict(float)
        self.owner = owner
    
    def update_balance(self, other_user: User, amount: float):
        # note we are not adding lock here because balance sheet is only used at splitservice and there we are using the lock
        self.balance[other_user]+=amount
    
    def show_balance_sheet(self):
        for user, amount in self.balance.items():
            if amount > 0:
                print(f"{self.owner.name} have to give {amount} rs. to {user.name}")
            elif amount < 0:
                print(f"{self.owner.name} have to take {-amount} rs. from {user.name}")