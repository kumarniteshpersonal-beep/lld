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

# facade that provides a simplified interface to the subsystems
class OrderFacade:
    def __init__(self):
        self.inventory_service = InventoryService()
        self.payment_service = PaymentService()
        self.shipping_service = ShippingService()

    def place_order(self, product_id, amount):
        if self.inventory_service.check_availability(product_id):
            payment_status = self.payment_service.process_payment(amount)
            if payment_status:
                return self.shipping_service.arrange_shipping(product_id, payment_status)
        return False