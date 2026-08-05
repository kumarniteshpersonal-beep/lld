from datetime import date
from enum import Enum
from payment_processor import PaymentProcessor

class ReservationStatus(Enum):
    ACTIVE = 1
    CANCELLED = 3

class Reservation:
    def __init__(self, car, customer, start_date: date, end_date: date):
        self.car = car
        self.customer = customer
        self.start_date = start_date
        self.end_date = end_date
        self.status = ReservationStatus.ACTIVE
        self.payment_method = None
    
    def cancel_reservation(self):
        self.status = ReservationStatus.CANCELLED
    
    def set_payment_method(self, payment_method: PaymentProcessor):
        self.payment_method = payment_method
    
    def get_price(self) -> float:
        total_days = (self.end_date - self.start_date)
        total_days = total_days.days
        return self.car.rental_price * total_days
    
    def process_payment(self):
        amount = self.get_price()
        if not self.payment_method:
            raise ValueError("please set the payment method first..")
        return self.payment_method.process_payment(amount=amount)