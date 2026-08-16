from user import User

class Expense:
    def __init__(self):
        self.paid_by = None
        self.description = ""
        self.split_strategy = None
        self.amount = 0.0
        self.additional_details = {}

    def calculate_splits(self):
        return self.split_strategy.calculate_splits(self)


class ExpenseBuilder:
    def __init__(self):
        self.expense = Expense()

    def set_amount(self, amount: float) -> 'ExpenseBuilder':
        self.expense.amount = amount
        return self

    def set_paid_by(self, paid_by: User) -> 'ExpenseBuilder':
        self.expense.paid_by = paid_by
        return self

    def set_description(self, description: str) -> 'ExpenseBuilder':
        self.expense.description = description
        return self

    def set_split_strategy(self, split_strategy) -> 'ExpenseBuilder':
        self.expense.split_strategy = split_strategy
        return self

    def set_additional_details(self, additional_details: dict):
        self.expense.additional_details = additional_details
        return self

    def build(self) -> Expense:
        return self.expense