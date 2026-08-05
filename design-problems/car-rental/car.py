from enum import Enum

class CarType(Enum):
    SEDAN = 1
    SUV = 2

class OperationalStatus(Enum):
    OPERATIONAL = 1
    UNDER_MAINTENANCE = 2

class Car:
    def __init__(self, plate_num: str, car_type: CarType, rental_price: float):
        self.plate_num = plate_num
        self.car_type = car_type
        self.operational_status = OperationalStatus.OPERATIONAL
        self.rental_price = rental_price
    
    def set_operational_status(self, status: OperationalStatus):
        self.operational_status = status
    
    def __repr__(self):
        return f"plate_num: {self.plate_num}, type: {self.car_type.name}"