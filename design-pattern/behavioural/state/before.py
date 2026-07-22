from enum import Enum

class TransportationMode(Enum):
    CAR = 1
    BIKE = 2
    WALK = 3

class DirectionService:
    def __init__(self, mode: TransportationMode = TransportationMode.CAR):
        self.mode = mode
    
    def get_eta(self, distance: float) -> float:
        if self.mode == TransportationMode.CAR:
            return distance / 60  # assuming average speed of 60 km/h
        elif self.mode == TransportationMode.BIKE:
            return distance / 15  # assuming average speed of 15 km/h
        elif self.mode == TransportationMode.WALK:
            return distance / 5   # assuming average speed of 5 km/h
        else:
            raise ValueError("Invalid transportation mode")

# client code
direction_service = DirectionService(TransportationMode.BIKE)
eta = direction_service.get_eta(30)
print(f"Estimated time of arrival: {eta} hours")

# problems:
# 1. If we want to add a new transportation mode (e.g., public transportation), we need to modify the DirectionService class, which violates the Open/Closed Principle.