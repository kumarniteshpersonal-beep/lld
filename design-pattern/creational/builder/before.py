class House:
    def __init__(self, walls, doors, windows):
        self.walls = walls
        self.doors = doors
        self.windows = windows

    def __str__(self):
        return f"House with {self.walls} walls, {self.doors} doors, and {self.windows} windows."

house = House(4, 2, 6)
print(house)