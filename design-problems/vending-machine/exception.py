class OutOfStockException(Exception):
    def __init__(self, product_id: str):
        super().__init__(f"Product with id {product_id} is out of stock.")

class InsufficientFundsException(Exception):
    pass
