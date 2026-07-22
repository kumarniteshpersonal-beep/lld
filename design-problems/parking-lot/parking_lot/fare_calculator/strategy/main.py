from abc import ABC, abstractmethod

class FareCalculationStrategy(ABC):
    @abstractmethod
    def calculate_fare(self, ticket, base_fare: float = 0.0) -> float:
        pass