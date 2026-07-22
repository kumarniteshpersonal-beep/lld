class House:
    def __init__(self):
        self.walls = None
        self.windows = None
        self.doors = None

    def __str__(self):
        return f"House with {self.walls}, {self.windows}, and {self.doors}."

class HouseBuilder:
    def __init__(self):
        self.house = House()

    def build_walls(self, walls) -> 'HouseBuilder':
        self.house.walls = walls
        return self

    def build_windows(self, windows) -> 'HouseBuilder':
        self.house.windows = windows
        return self

    def build_doors(self, doors) -> 'HouseBuilder':
        self.house.doors = doors
        return self

    def build(self) -> House:
        return self.house

# client code
builder = HouseBuilder()
house = builder.build_walls(4).build_windows(6).build_doors(2).build()
print(house)