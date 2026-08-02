from exception import OutOfStockException

class Product:
    def __init__(self, id: str, name: str, price: int, quantity: int = 0):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"Product(id={self.id}, name={self.name}, price={self.price}, quantity={self.quantity})"

class ProductInventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product: Product):
        self.products[product.id] = product

    def restock_product(self, id: str, quantity: int):
        if id in self.products:
            self.products[id].quantity += quantity
    
    def get_all_products(self):
        return self.products.values()
    
    def has_product(self, id: str) -> bool:
        return id in self.products and self.products[id].quantity > 0

    def get_product(self, id: str) -> Product:
        if self.has_product(id):
            return self.products[id]
        else:
            raise Exception(f"Product with id {id} is not available in the inventory.")

    def buy_product(self, id: str):
        if self.has_product(id):
            self.products[id].quantity -= 1
        else:
            raise OutOfStockException(id)

    def dispense(self, id: str):
        self.buy_product(id)
        print(f"Dispensing product: {self.products[id].name}")