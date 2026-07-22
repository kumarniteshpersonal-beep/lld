from parking_lot.vehicle import Vehicle, VehicleType

class Bike(Vehicle):
    def __init__(self, license_plate):
        super().__init__(license_plate)

    def get_vehicle_type(self) -> VehicleType:
        return VehicleType.SMALL