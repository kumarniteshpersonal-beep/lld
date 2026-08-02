from machine import VendingMachine
from product_inventory import Product
from cash_inventory import DenominationType

class VendingMachineDemo:
    @staticmethod
    def main():
        vending_machine = VendingMachine()
        vending_machine.add_product(Product("soda#1","Soda", 23, 10))
        vending_machine.add_product(Product("chips#1","Chips", 10, 20))
        vending_machine.add_product(Product("candy#1","Candy", 5, 30))
        vending_machine.add_money({DenominationType.ONE: 200, DenominationType.TWO: 25, DenominationType.FIVE: 20, DenominationType.TEN: 12})
        
        # list all products
        products = vending_machine.list_products()
        print(products)

        print(vending_machine.cash_inventory.cash_cnt)
        # ---------- transaction 1 start ----------
        transaction = vending_machine.create_transaction() # create a transaction
        vending_machine.select_product(transaction, "soda#1") # select product
        vending_machine.insert_money(transaction, DenominationType.TEN) # insert money
        vending_machine.insert_money(transaction, DenominationType.TEN) # insert money
        vending_machine.insert_money(transaction, DenominationType.TEN) # insert money

        # vending_machine.cancel(transaction) # click on cancel button
        vending_machine.dispense(transaction) # dispense the product
        # --------- transaction 1 ends ----------
        print(vending_machine.cash_inventory.cash_cnt)

VendingMachineDemo.main()