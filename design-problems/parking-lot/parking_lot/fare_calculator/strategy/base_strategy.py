from parking_lot.fare_calculator.strategy import FareCalculationStrategy
from parking_lot.vehicle import VehicleType

class BaseFareCalculationStrategy(FareCalculationStrategy):
    RATES_PER_MINUTE = {
        VehicleType.SMALL: 1.0,
        VehicleType.MEDIUM: 2.0,
        VehicleType.LARGE: 3.0
    }
    def calculate_fare(self, ticket, base_fare: float = 0.0) -> float:
        _timedelta = ticket.get_parking_duration().total_seconds() / 60
        return base_fare + (_timedelta * self.RATES_PER_MINUTE[ticket.vehicle.get_vehicle_type()])