from enum import Enum
from abc import ABC, abstractmethod

class TransportationMode(Enum):
    CAR = 1
    BIKE = 2
    WALK = 3

class TransportMeans(ABC): # state interface
    @abstractmethod
    def get_eta(self, distance: float) -> float:
        pass

class Car(TransportMeans): # concrete state
    def get_eta(self, distance: float) -> float:
        return distance / 60  # assuming average speed of 60 km/h

class Bike(TransportMeans): # concrete state
    def get_eta(self, distance: float) -> float:
        return distance / 15  # assuming average speed of 15 km/h

class Walk(TransportMeans): # concrete state
    def get_eta(self, distance: float) -> float:
        return distance / 5  # assuming average speed of 5 km/h

class DirectionService: # context which holds context of the state
    def __init__(self, transport_means: TransportMeans):
        self.transport_means = transport_means

    def get_eta(self, distance: float) -> float:
        return self.transport_means.get_eta(distance)

    def set_transport_mode(self, transport_means: TransportMeans):
        self.transport_means = transport_means

# client code
direction_service = DirectionService(Bike())
eta = direction_service.get_eta(30)
print(f"Estimated time of arrival: {eta} hours")

# change transport mode
direction_service.set_transport_mode(Car())
eta = direction_service.get_eta(30)
print(f"Estimated time of arrival: {eta} hours")

# Hence, in state pattern context store reference of state interface and client can change the state at runtime without modifying the context class.
# Hence state can easily be changed which in turn allows for dynamic behavior in the application.