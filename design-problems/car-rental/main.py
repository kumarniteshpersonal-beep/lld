from car_rental_svc import CarRentalService
from car import Car, CarType
from customer import Customer
from datetime import date, timedelta
from payment_processor import WalletPaymentProcessor, CreditCardPaymentProcessor

class CarRentalSystemDemo:
    @staticmethod
    def main():
        service = CarRentalService()

        # add 2 sedans and 3 suvs
        car1 = Car(plate_num="UP15ABCD", car_type=CarType.SEDAN, rental_price=550)
        car2 = Car(plate_num="UP14ABCD", car_type=CarType.SEDAN, rental_price=950)
        service.add_car(car1)
        service.add_car(car2)

        car3 = Car(plate_num="MP15ABCD", car_type=CarType.SUV, rental_price=1550)
        car4 = Car(plate_num="TL15ABCD", car_type=CarType.SUV, rental_price=2000)
        service.add_car(car3)
        service.add_car(car4)

        # add customer
        customer1 = Customer(name="Nitesh", license_number="UPTTNITY")
        service.add_customer(customer1)

        # make some reservations
        reservation1 = service.make_reservation(car1, customer1, date.today(), date.today() + timedelta(days=4)) # 5 aug to 9 aug
        reservation1.set_payment_method(WalletPaymentProcessor())
        reservation1.process_payment() # if payment errored we can cancel the reservation
        # service.make_reservation(car1, customer1, date.today() + timedelta(2), date.today() + timedelta(days=5)) # 7 aug to 10 aug will give overlap error
        available_sedan_cars = service.search_cars(CarType.SEDAN, date.today(), date.today() + timedelta(days=4)) # search cars available between 5 aug and 9 aug
        print(available_sedan_cars)
        available_sedan_cars = service.search_cars(CarType.SEDAN, date.today() + timedelta(days=5), date.today() + timedelta(days=7)) # search cars available between 10 aug and 12 aug
        print(available_sedan_cars)

        reservation2 = service.make_reservation(car2, customer1, date.today() + timedelta(days=5), date.today() + timedelta(days=7)) # 10 to 12 aug
        reservation2.set_payment_method(CreditCardPaymentProcessor()) # adding payment strategy
        reservation2.process_payment()

        # search available sedan cars between 5 aug and 20 aug - no one should be there
        available_sedan_cars = service.search_cars(CarType.SEDAN, date.today(), date.today() + timedelta(days=15))
        print(available_sedan_cars)

        service.cancel_reservation(reservation2)

        # again search available sedan cars between 5 aug and 20 aug - no one should be there
        available_sedan_cars = service.search_cars(CarType.SEDAN, date.today(), date.today() + timedelta(days=15))
        print(available_sedan_cars)

CarRentalSystemDemo.main()