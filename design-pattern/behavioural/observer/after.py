from abc import ABC, abstractmethod

# observer interface
class DeviceObserver(ABC):
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def show_weather(self, weather):
        pass

class MobileApp(DeviceObserver):
    def show_weather(self, weather):
        print(f"{self.name} Mobile App: Current weather is {weather}.")

class DesktopApp(DeviceObserver):
    def show_weather(self, weather):
        print(f"{self.name} Desktop App: Current weather is {weather}.")

# subject interface
class WeatherStationSubject(ABC):
    @abstractmethod
    def register_observer(self, observer: DeviceObserver):
        pass
    
    @abstractmethod
    def remove_observer(self, observer: DeviceObserver):
        pass
    
    @abstractmethod
    def notify_observers(self):
        pass

class WeatherStation(WeatherStationSubject):
    def __init__(self):
        self.observers = []
        self.weather = 10
    
    def register_observer(self, observer: DeviceObserver):
        self.observers.append(observer)
    
    def remove_observer(self, observer: DeviceObserver):
        self.observers.remove(observer)
    
    def notify_observers(self):
        for observer in self.observers:
            observer.show_weather(self.weather)
    
    def update_weather(self, weather):
        self.weather = weather
        self.notify_observers()

# client code
weather_station = WeatherStation()
mobile_app = MobileApp("Weather")
desktop_app = DesktopApp("Weather")

weather_station.register_observer(mobile_app)
weather_station.register_observer(desktop_app)

weather_station.update_weather(25)