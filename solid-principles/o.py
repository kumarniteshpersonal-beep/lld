# open/closed principle - states that software entities (classes, modules, functions, etc.) should be open for extension but closed for modification.

# without opnen/closed principle
class AreaCalculator:
    def calculate_area(self, shape):
        if shape['type'] == 'circle':
            return 3.14 * (shape['radius'] ** 2)
        elif shape['type'] == 'rectangle':
            return shape['width'] * shape['height']
        else:
            raise ValueError('Unknown shape type')


calculator = AreaCalculator()
print(calculator.calculate_area({'type': 'circle', 'radius': 5}))
print(calculator.calculate_area({'type': 'rectangle', 'width': 4, 'height': 5}))

# problems:
# 1. now to add new shape, we need to modify the AreaCalculator class.
# 2. we should avoid modifying existing code, as it can introduce bugs and break existing functionality.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class AreaCalculator:
    @staticmethod
    def calculate_area(shape: Shape):
        return shape.area()

calculator = AreaCalculator()
print(calculator.calculate_area(Circle(5)))
print(calculator.calculate_area(Rectangle(4, 5)))