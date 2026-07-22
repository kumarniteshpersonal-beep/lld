# Liskov Substitution Principle - states that objects of a superclass should be replaceable with objects of a subclass without affecting the correctness of the program.
from abc import ABC, abstractmethod

class Bird(ABC):
    @abstractmethod
    def fly(self):
        pass

class Sparrow(Bird):
    def fly(self):
        return "Sparrow is flying"

class Ostrich(Bird):
    def fly(self):
        raise NotImplementedError("Ostriches can't fly")

def let_bird_fly(bird: Bird):
    print(bird.fly())

for bird in [Sparrow(), Ostrich()]:
    let_bird_fly(bird)

# problems:
# 1. So the problem is we want the all our subclasses should be replacable by superclass without affecting the correctness of the program. 
# 2. In this case, the Ostrich class violates the Liskov Substitution Principle because it cannot be substituted for the Bird class without causing an error.


class Bird(ABC): # because all bird can't fly
    pass

class BirdThatCanFly(Bird):
    @abstractmethod
    def fly(self):
        pass

class Sparrow(BirdThatCanFly):
    def fly(self):
        return "Sparrow is flying"

class Ostrich(Bird):
    pass

def let_bird_fly(bird: BirdThatCanFly):
    print(bird.fly())

for bird in [Sparrow(), Ostrich()]:
    if isinstance(bird, BirdThatCanFly):
        let_bird_fly(bird)
    else:
        print(f"{bird.__class__.__name__} can't fly")