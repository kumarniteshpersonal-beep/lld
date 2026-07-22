from abc import ABC, abstractmethod

# component interface
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

# decorator base class that wraps a pizza and delegates calls to it
class DecoratorPizza(BasePizza):
    def __init__(self, pizza: BasePizza):
        self.pizza = pizza

    def get_description(self):
        return self.pizza.get_description()

    def get_cost(self):
        return self.pizza.get_cost()

class CheeseDecorator(DecoratorPizza):
    def get_description(self):
        return super().get_description() + " + Cheese"

    def get_cost(self):
        return super().get_cost() + 2.0

class OliveDecorator(DecoratorPizza):
    def get_description(self):
        return super().get_description() + " + Olive"

    def get_cost(self):
        return super().get_cost() + 3.0

class OnionDecorator(DecoratorPizza):
    def get_description(self):
        return super().get_description() + " + Onion"

    def get_cost(self):
        return super().get_cost() + 1.0

# client code
pizza = PlainPizza()
print(pizza.get_description(), pizza.get_cost())

# I want to make cheese + onion + olive pizza, then I can do it like this
pizza = PlainPizza()
pizza = CheeseDecorator(pizza)
pizza = OnionDecorator(pizza)
pizza = OliveDecorator(pizza)
print(pizza.get_description(), pizza.get_cost())