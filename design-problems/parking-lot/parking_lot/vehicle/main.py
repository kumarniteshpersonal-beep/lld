from abc import ABC, abstractmethod
from enum import Enum

class VehicleType(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class Vehicle(ABC):
    def __init__(self, license_plate):
        self.license_plate = license_plate

    @abstractmethod
    def get_vehicle_type(self) -> VehicleType:
        pass

    def get_license_plate(self) -> str:
        return self.license_plate