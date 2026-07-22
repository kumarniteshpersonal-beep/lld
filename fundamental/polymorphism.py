# Runtime Polymorphism/Method Overriding in Python
class Animal:
    def speak(self):
        print("Animal speaks")
    
class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

def animal_sound(animal: Animal):
    animal.speak() # polymorphic behavior, the method called depends on the type of object passed

animal_sound(Dog())
animal_sound(Cat())
animal_sound(Animal())

# Operator Overloading in Python
class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    
    def __add__(self, other): # overloading the + operator
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        return NotImplemented

point1 = Point(1, 2)
point2 = Point(3, 4)
result = point1 + point2 # using overloaded + operator
print(f"Result of adding points: ({result.x}, {result.y})") # so top level syntax plus calls the __add__ method of the Point class.

# Duck Typing in Python (only relevant in dynamically typed languages like Python which cares about the behavior of an object rather than its type)
# Duck typing is a behavior-based form of polymorphism where an object is considered valid if it provides the required methods, regardless of its actual type.
class Bird:
    def fly(self):
        print("Bird is flying")

class Airplane:
    def fly(self):
        print("Airplane is flying")

def let_it_fly(flying_thing):
    flying_thing.fly()

let_it_fly(Bird())
let_it_fly(Airplane())

print(isinstance(Bird(), Airplane)) # False, they are different types but both can fly