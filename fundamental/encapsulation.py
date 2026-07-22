# class -> blueprint for creating objects
class Car:
    wheels = 2 # class variable

    @classmethod
    def change_wheels(cls, new_wheels): # class method to access and modify class variable
        cls.wheels = new_wheels

    @staticmethod
    def info(): # static method which does not access class or instance variables
        return "This is a car class"
    
    def __init__(self, car_price: int = 0, car_name: str = "Unknown", model_year: int = 2020):
        self._price = car_price # protected instance variable can be accessed by subclasses or within the class
        self.__name = car_name # private instance variable can only be accessed within the class
        self.model_year = model_year # public instance variable can be accessed from anywhere
    
    def get_name(self): # public method to access private instance variable
        return self.__name
    
    @property
    def price(self): # getter method for protected instance variable
        return self._price
    
    @price.setter
    def price(self, new_price): # setter method for protected instance variable
        if new_price < 0:
            raise ValueError("Price cannot be negative")
        self._price = new_price


# creating an object of the Car class
my_car = Car(20000, "Toyota", 2021)
print(my_car.model_year) # accessing public instance variable
print(my_car._price) # accessing protected instance variable (not recommended)
# print(my_car.__name) # accessing private instance variable (will raise an error)
print(my_car.get_name()) # accessing private instance variable using public method
print(Car.wheels) # accessing class variable
Car.change_wheels(4) # modifying class variable using class method
print(Car.wheels) # accessing modified class variable
print(Car.info()) # calling static method
my_car.price = 25000 # using setter method to modify protected instance variable
print(my_car.price) # using getter method to access modified protected instance variable
