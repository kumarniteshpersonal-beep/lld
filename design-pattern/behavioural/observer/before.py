from abc import ABC, abstractmethod

# consumer
class Device(ABC):
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def show_weather(self, weather):
        pass

class MobileApp(Device):
    def show_weather(self, weather):
        print(f"{self.name} Mobile App: Current weather is {weather}.")

class DesktopApp(Device):
    def show_weather(self, weather):
        print(f"{self.name} Desktop App: Current weather is {weather}.")

# producer
class WeatherStation:
    def __init__(self):
        self.devices = [MobileApp("Weather"), DesktopApp("Weather")]
        self.weather = 10
    
    def update_weather(self, weather):
        self.weather = weather
        for device in self.devices:
            device.show_weather(weather)

# client code
weather_station = WeatherStation()
weather_station.update_weather(25)