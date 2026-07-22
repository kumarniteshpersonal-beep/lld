from abc import ABC, abstractmethod

class BasePizza(ABC):
    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_cost(self):
        pass

class PlainPizza(BasePizza):
    def get_description(self):
        return "Plain Pizza"

    def get_cost(self):
        return 4.0

class CheesePizza(PlainPizza):
    def get_description(self):
        return super().get_description() + " + Cheese"

    def get_cost(self):
        return super().get_cost() + 2.0

class CornPizza(PlainPizza):
    def get_description(self):
        return super().get_description() + " + Corn"

    def get_cost(self):
        return super().get_cost() + 6.0

class OnionPizza(PlainPizza):
    def get_description(self):
        return super().get_description() + " + Onion"

    def get_cost(self):
        return super().get_cost() + 8.0

class CheeseOnionPizza(PlainPizza):
    def get_description(self):
        return super().get_description() + " + Cheese + Onion"

    def get_cost(self):
        return super().get_cost() + 2.0 + 8.0

class CornOnionPizza(PlainPizza):
    def get_description(self):
        return super().get_description() + " + Corn + Onion"

    def get_cost(self):
        return super().get_cost() + 6.0 + 8.0

class CheeseCornOnionPizza(PlainPizza):
    def get_description(self):
        return super().get_description() + " + Cheese + Corn + Onion"

    def get_cost(self):
        return super().get_cost() + 2.0 + 6.0 + 8.0

# client code
cheese_onion_pizza = CheeseOnionPizza()
print(cheese_onion_pizza.get_description(), cheese_onion_pizza.get_cost())

corn_onion_pizza = CornOnionPizza()
print(corn_onion_pizza.get_description(), corn_onion_pizza.get_cost()) 

cheese_corn_onion_pizza = CheeseCornOnionPizza()
print(cheese_corn_onion_pizza.get_description(), cheese_corn_onion_pizza.get_cost())

# problems:
# 1. Now there is class explosion, if we want to add a new topping (e.g., pepperoni), then we need to create new classes for all possible combinations of toppings which is not scalable and maintainable.
# 2. exponential growth of classes, if we have n toppings, then we need to create 2^n classes to cover all possible combinations of toppings which is not practical.