from collections import defaultdict
from customer import Customer
from car import Car, CarType
from reservation import Reservation
from datetime import date
from threading import Lock

class CarRentalService:
    def __init__(self):
        self.cars_by_type = defaultdict(list) # indexed by type property
        self.reservations_by_car = defaultdict(list) # <plate_num: [reservations]> only storing active rservations
        self._reservation_lock = defaultdict(Lock) # lock for each car
        self.customers = []
    
    def set_payment_processor(self, payment_processor):
        self.payment_processor = payment_processor

    def add_car(self, car: Car):
        car_type = car.car_type
        car_plate_num = car.plate_num
        self._reservation_lock[car_plate_num] = Lock()
        self.cars_by_type[car_type].append(car)
    
    def add_customer(self, customer: Customer):
        self.customers.append(customer)
    
    def process_payment(self, reservation: Reservation) -> bool:
        return reservation.process_payment()
    
    def _lowest_reservation_index(self, car: Car, start_date: date, end_date: date) -> int:
        ans = -1
        reservations = self.reservations_by_car[car.plate_num]
        l,h = 0,len(reservations)-1

        while l<=h:
            mid = (l+h)//2
            if start_date > reservations[mid].end_date:
                l = mid+1
                ans = mid
            elif end_date < reservations[mid].start_date:
                h = mid-1
            else:
                # overlap case we can't make reservations
                ans = -2
                break
        
        # ans is -1 in cases when:
        # 1. no reservations yet
        # 2. when my end_date is lesser then the first reservation
        # 3. in cases when there is overlap we will return -2
        return ans

    def _can_make_reservation(self, car: Car, start_date: date, end_date: date) -> bool:
        return self._lowest_reservation_index(car, start_date, end_date)!=-2

    def search_cars(self, type: CarType, start_date: date, end_date: date) -> list[Car]:
        cars_by_type = self.cars_by_type[type]
        filtered_list = []
        for car in cars_by_type:
            if self._can_make_reservation(car, start_date, end_date):
                filtered_list.append(car)
        return filtered_list

    def make_reservation(self, car: Car, customer: Customer, start_date: date, end_date: date) -> Reservation:
        car_plate_num = car.plate_num

        with self._reservation_lock[car_plate_num]:
            lowest_index_to_reserve_for_car = self._lowest_reservation_index(car, start_date, end_date)
            if lowest_index_to_reserve_for_car==-2:
                raise ValueError("time is overlapping with other reservation..")
            new_reservation = Reservation(car, customer, start_date, end_date)
            self.reservations_by_car[car_plate_num].insert(lowest_index_to_reserve_for_car+1, new_reservation)
            return new_reservation

    
    def cancel_reservation(self, reservation: Reservation):
        car = reservation.car
        car_plate_num = car.plate_num

        with self._reservation_lock[car_plate_num]:
            reservations = self.reservations_by_car[car_plate_num]

            idx = 0
            for _reservation in self.reservations_by_car[car_plate_num]:
                if _reservation==reservation:
                    break
                idx+=1
            
            if idx < len(reservations):
                reservations[idx].cancel_reservation()
                del reservations[idx]