# subsystems
class InventoryService:
    def check_availability(self, product_id):
        print(f"Checking inventory for product {product_id}")
        return True  # Assume the product is available

class PaymentService:
    def process_payment(self, amount):
        print(f"Processing payment of ${amount}")
        return True  # Assume payment is successful

class ShippingService:
    def arrange_shipping(self, product_id, payment_status):
        print(f"Arranging shipping for product {product_id} where payment status is {payment_status}")
        return True  # Assume shipping is arranged

# client code to place an order

def place_order(product_id, amount):
    inventory_service = InventoryService()
    payment_service = PaymentService()
    shipping_service = ShippingService()

    # The client has to interact with all three services directly, which can be complex and error-prone
    inventory_service.check_availability(product_id)
    shipping_service.arrange_shipping(product_id, payment_service.process_payment(amount))

# problem:

# 1. tomorrow if any of the services change their interface, then I have to change the client code as well, which is not ideal
# 2. the client code is tightly coupled to the subsystems, which makes it harder