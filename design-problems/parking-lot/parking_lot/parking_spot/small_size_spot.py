from parking_lot.parking_spot import ParkingSpot
from parking_lot.vehicle import VehicleType

class SmallSizeSpot(ParkingSpot):
    def __init__(self, spot_id):
        super().__init__(spot_id)

    def get_spot_size(self) -> VehicleType:
        return VehicleType.SMALL