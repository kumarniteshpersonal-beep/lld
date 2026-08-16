class User:
    def __init__(self,user_id: str, name: str):
        from balance_sheet import BalanceSheet

        self.user_id = user_id
        self.name = name
        self.balance_sheet = BalanceSheet(self)
    
    def __hash__(self):
        return hash(self.user_id)
    
    def __repr__(self):
        return self.name