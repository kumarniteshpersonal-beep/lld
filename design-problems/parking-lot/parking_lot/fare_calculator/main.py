from parking_lot.fare_calculator.strategy import FareCalculationStrategy

class FareCalculator:
    def __init__(self):
        self.strategy = None
    
    def set_strategy(self, strategy: FareCalculationStrategy):
        self.strategy = strategy

    def calculate_fare(self, ticket, base_fare: float = 0.0) -> float:
        if not self.strategy:
            raise ValueError("Fare calculation strategy is not set.")
        return self.strategy.calculate_fare(ticket, base_fare)