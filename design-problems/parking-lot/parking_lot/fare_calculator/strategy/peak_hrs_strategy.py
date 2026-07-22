from parking_lot.fare_calculator.strategy import FareCalculationStrategy

class PeakHoursFareCalculationStrategy(FareCalculationStrategy):
    def calculate_fare(self, ticket, base_fare: float = 0.0) -> float:
        return base_fare * 1.4
