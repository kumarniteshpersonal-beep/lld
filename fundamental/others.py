# Association - Here Car uses Engine.
class Engine:
    def start(self):
        print("Engine starting...")

class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()
        print("Car is ready to go!")

my_car = Car()
my_car.start()

# Aggregation - Here Driver has a Car, but Car can exist independently of Driver
class Driver:
    def drive(self, car: Car):
        car.start()

driver = Driver()
driver.drive(my_car)

# Composition - Here Kitchen is a part of House, and the Kitchen cannot exist without the House
class Kitchen:
    def __init__(self):
        self.appliances = []

    def add_appliance(self, appliance):
        self.appliances.append(appliance)

class House:
    def __init__(self):
        self.kitchen = Kitchen() # House has a Kitchen, and the Kitchen cannot exist without the House