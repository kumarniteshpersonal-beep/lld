from state import VendingMachineState, IdleState
from cash_inventory import DenominationType
from collections import defaultdict

class Transaction:
    def __init__(self, machine):
        self.state: VendingMachineState = IdleState(self)
        self.machine = machine
        self.selected_product_id = None
        self.inserted_money = 0
        self.inserted_money_denominations = defaultdict(int)  # Track inserted money denominations
    
    def set_selected_product(self, product_id: str):
        self.selected_product_id = product_id
    
    def add_money(self, amount: DenominationType):
        self.inserted_money += amount.value
        self.inserted_money_denominations[amount] += 1  # Track the count of each denomination inserted
    
    def reset(self):
        self.selected_product_id = None
        self.inserted_money = 0
        self.state = IdleState(self)
        self.inserted_money_denominations = defaultdict(int)  # Reset the denomination tracker

    def set_state(self, state: VendingMachineState):
        self.state = state
    
    def insert_money(self, amount: int):
        self.state.insert_money(amount)
    
    def select_product(self, product_id: str):
        self.state.select_product(product_id)
    
    def dispense(self):
        self.state.dispense()
    
    def cancel(self):
        self.state.cancel()