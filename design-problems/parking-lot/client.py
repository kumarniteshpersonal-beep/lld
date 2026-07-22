from parking_lot import ParkingLotFacade
from parking_lot.parking_manager import ParkingManager
from parking_lot.fare_calculator import FareCalculator
from parking_lot.vehicle import VehicleType, Bike, Car, Bus
from datetime import datetime, timedelta

# init parking lot facade
parking_lot_service = ParkingLotFacade(
    fare_calculator=FareCalculator(),
    parking_manager=ParkingManager()
)

# parking spots initialization
parking_lot_service.init_spots({
    VehicleType.SMALL: 10,
    VehicleType.MEDIUM: 10,
    VehicleType.LARGE: 2
})

# park some vehicles
suv_car = Car("KA-01-12345")
sedan_car = Car("KA-01-54321")
hero_honda_bike = Bike("KA-01-67890")
bus1 = Bus("KA-01-09876")
bus2 = Bus("KA-01-09877")
tractor = Bus("KA-01-09878")

suv_ticket = parking_lot_service.park_vehicle(suv_car)
bus_ticket = parking_lot_service.park_vehicle(bus1)
bus_ticket_2 = parking_lot_service.park_vehicle(bus2)
# tractor_ticket = parking_lot_service.park_vehicle(tractor) # no spot available for tractor

# unpark and get prices for suv car after 2 hours
suv_ticket.set_end_time(datetime.now() + timedelta(minutes=120))
print("Fare for suv car: " + str(parking_lot_service.unpark_and_calculate_fare(suv_ticket)))

# unpark and get prices for bus1 after 3 hours
bus_ticket.set_end_time(datetime.now() + timedelta(minutes=180))
print("Fare for bus1: " + str(parking_lot_service.unpark_and_calculate_fare(bus_ticket)))