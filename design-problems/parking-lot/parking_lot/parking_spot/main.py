from abc import ABC, abstractmethod

class ParkingSpot(ABC):
    def __init__(self, spot_id):
        self.spot_id = spot_id
        self.vehicle = None
    
    def is_available(self):
        return self.vehicle is None
    
    def vacate(self):
        self.vehicle = None
    
    def park_vehicle(self, vehicle):
        if self.is_available():
            self.vehicle = vehicle
            return True
        return False

    @abstractmethod
    def get_spot_size(self):
        pass