from parking_lot.fare_calculator.strategy.peak_hrs_strategy import PeakHoursFareCalculationStrategy
from parking_lot.fare_calculator.strategy.base_strategy import BaseFareCalculationStrategy
from parking_lot.ticket import Ticket
from datetime import datetime

class ParkingLotFacade:
    def __init__(self, fare_calculator=None, parking_manager=None):
        self.fare_calculator = fare_calculator
        self.parking_manager = parking_manager
    
    def init_spots(self, initial_available_spots):
        self.parking_manager.init_spots(initial_available_spots)
    
    def park_vehicle(self, vehicle) -> Ticket:
        return self.parking_manager.park(vehicle)

    def is_peak_hours(self) -> bool:
        current_time = datetime.now()
        if current_time.hour >= 8 and current_time.hour < 11:
            return True
        return False

    def unpark_and_calculate_fare(self, ticket) -> float:
        self.parking_manager.unpark(ticket.vehicle)
        self.fare_calculator.set_strategy(BaseFareCalculationStrategy())
        fare = self.fare_calculator.calculate_fare(ticket,0.0)
        if self.is_peak_hours():
            self.fare_calculator.set_strategy(PeakHoursFareCalculationStrategy())
            fare = self.fare_calculator.calculate_fare(ticket, fare)
        return fare