class TV:
    def turn_on(self):
        print("TV ON")

    def turn_off(self):
        print("TV OFF")

class Remote:
    def __init__(self, tv: TV):
        self.tv = tv

    def turn_on_tv(self):
        self.tv.turn_on()

    def turn_off_tv(self):
        self.tv.turn_off()

# client code
tv = TV()
remote = Remote(tv)
remote.turn_on_tv()
remote.turn_off_tv()

# problems:
# 1. The Remote class is tightly coupled to the TV class, which makes it difficult to extend the functionality of the Remote class to control other devices (like AC, Sound System, etc.)
# 2. If we want to add new functionality to the Remote class (like volume control, channel control, etc.), we would have to modify the Remote class, which violates the Open/Closed Principle.