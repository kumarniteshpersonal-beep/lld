from abc import ABC, abstractmethod

class VendingMachineState(ABC):
    def __init__(self, transaction):
        self.transaction = transaction

    @abstractmethod
    def select_product(self, product_id: str):
        pass

    @abstractmethod
    def insert_money(self, amount: int):
        pass

    @abstractmethod
    def dispense(self):
        pass

    @abstractmethod
    def cancel(self):
        pass

class IdleState(VendingMachineState):
    def select_product(self, product_id: str):
        product_inventory = self.transaction.machine.product_inventory
        # check if the product exists in the inventory
        if product_inventory.has_product(product_id):
            self.transaction.set_selected_product(product_id)
        else:
            raise Exception(f"Product with id {product_id} is not available in the inventory.")
        # change the state to ProductSelectedState
        self.transaction.set_state(ProductSelectedState(self.transaction))

    def insert_money(self, amount: int):
        raise Exception("Please select the product first.")
    
    def dispense(self):
        raise Exception("Please select the product and complete the payment first.")
    
    def cancel(self):
        print("transaction still in idle state so no money to return..")

class ProductSelectedState(VendingMachineState):
    def select_product(self, product_id: str):
        raise Exception("Product has already been selected. Please proceed to payment or cancel the transaction.")

    def insert_money(self, amount: int):
        self.transaction.add_money(amount)
        product_selected = self.transaction.selected_product_id
        product_inventory = self.transaction.machine.product_inventory
        product_price = product_inventory.get_product(product_selected).price

        if self.transaction.inserted_money >= product_price:
            print("sufficient money inserted, proceed to dispense the product.")
            self.transaction.set_state(HasMoneyState(self.transaction))
    
    def dispense(self):
        raise Exception("Please complete the payment first.")
    
    def cancel(self):
        total_money_inserted = self.transaction.inserted_money
        if total_money_inserted > 0:
            print(f"Returning ${total_money_inserted} to the user.")
            self.transaction.reset()
        else:
            print("No money to return.")

class HasMoneyState(VendingMachineState):
    def select_product(self, product_id: str):
        print("product already selected.")

    def insert_money(self, amount: int):
        print("amount already inserted, please proceed to dispense the product or cancel the transaction.")
    
    def dispense(self):
        with self.transaction.machine._lock:  # Acquire the lock for the purchase operation
            total_money_inserted = self.transaction.inserted_money
            product_selected = self.transaction.selected_product_id
            product_inventory = self.transaction.machine.product_inventory
            cash_inventory = self.transaction.machine.cash_inventory

            if total_money_inserted >= product_inventory.get_product(product_selected).price:
                change_to_return = total_money_inserted - product_inventory.get_product(product_selected).price
                # check can we dispense the change or not
                if not cash_inventory.can_dispense(change_to_return):
                    print("Unable to dispense change. hence cancelling the transaction and returning the money to the user.")
                    self.cancel()
                    return

                if not product_inventory.has_product(product_selected):
                    print("Product is out of stock. hence cancelling the transaction and returning the money to the user.")
                    self.cancel()
                    return

                product_inventory.dispense(product_selected)
                if change_to_return > 0:
                    try:
                        cash_inventory.dispense(change_to_return)
                    except Exception as e:
                        print(f"Unable to return change: {e}")
                        product_inventory.restock_product(product_selected, 1)  # Restock the product since we couldn't complete the transaction
                        self.cancel()
                        return
                # add the inserted money to the cash inventory
                cash_inventory.add_money(self.transaction.inserted_money_denominations)
                self.transaction.reset()
            else:
                print("Insufficient money inserted. Please insert more money or cancel the transaction.")
    
    def cancel(self):
        total_money_inserted = self.transaction.inserted_money
        if total_money_inserted > 0:
            print(f"Returning ${total_money_inserted} to the user.")
            self.transaction.reset()
        else:
            print("No money to return.")