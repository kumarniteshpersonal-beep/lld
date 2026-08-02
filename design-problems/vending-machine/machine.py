from product_inventory import ProductInventory
from cash_inventory import CashInventory
from transaction import Transaction
from threading import Lock

class VendingMachine:
    def __init__(self):
        self.product_inventory = ProductInventory()
        self.cash_inventory = CashInventory()
        self._lock = Lock()  # Lock for synchronizing purchase operations

    def add_product(self, product):
        self.product_inventory.add_product(product)

    def add_money(self, cash_cnt: dict):
        self.cash_inventory.add_money(cash_cnt)
    
    def list_products(self):
        return self.product_inventory.get_all_products()

    def create_transaction(self):
        transaction = Transaction(self)
        return transaction
    
    def select_product(self, transaction: Transaction, product_id: str):
        transaction.select_product(product_id)
        print("product selected: ", product_id)
    
    def insert_money(self, transaction: Transaction, denomination_type):
        transaction.insert_money(denomination_type)

    def dispense(self, transaction: Transaction):
        transaction.dispense()
    
    def cancel(self, transaction: Transaction):
        transaction.cancel()