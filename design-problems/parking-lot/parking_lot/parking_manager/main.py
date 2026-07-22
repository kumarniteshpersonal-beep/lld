from datetime import datetime
from parking_lot.ticket import Ticket
from parking_lot.parking_spot import ParkingSpot
from parking_lot.vehicle import VehicleType, Vehicle
from parking_lot.parking_spot import SmallSizeSpot, MediumSizeSpot, BigSizeSpot

class ParkingManager:
    def __init__(self):
        self.available_spots = {}
        self.vehicle_to_spot_map = {}
    
    def init_spots(self, initial_available_spots):
        for key in initial_available_spots:
            if key==VehicleType.SMALL:
                self.available_spots[key] = [SmallSizeSpot("small_" + str(spot_id)) for spot_id in range(initial_available_spots[key])]
            elif key==VehicleType.MEDIUM:
                self.available_spots[key] = [MediumSizeSpot("medium_" + str(spot_id)) for spot_id in range(initial_available_spots[key])]
            elif key==VehicleType.LARGE:
                self.available_spots[key] = [BigSizeSpot("large_" + str(spot_id)) for spot_id in range(initial_available_spots[key])]

    def park(self, vehicle) -> Ticket:
        spot = self.find_spot_for_vehicle(vehicle.get_vehicle_type())
        if spot is None:
            raise Exception("No parking spot available for vehicle type: " + str(vehicle.get_vehicle_type()))
        spot.park_vehicle(vehicle)
        self.vehicle_to_spot_map[vehicle.get_license_plate()] = spot
        ticket = Ticket(id(spot),vehicle,datetime.now())
        return ticket

    def unpark(self, vehicle: Vehicle) -> float:
        spot = self.vehicle_to_spot_map.get(vehicle.get_license_plate(),None)
        if spot is None:
            raise Exception("Vehicle with license plate: " + str(vehicle.get_license_plate()) + " is not parked")
        spot.vacate()
        del self.vehicle_to_spot_map[vehicle.get_license_plate()]
        self.available_spots[spot.get_spot_size()].append(spot)


    def find_spot_for_vehicle(self, vehicle_type) -> ParkingSpot:
        for key in [VehicleType.SMALL, VehicleType.MEDIUM, VehicleType.LARGE]:
            if key.value >= vehicle_type.value and len(self.available_spots[key]) > 0:
                return self.available_spots[key].pop(0)
        return None