import random

class Player:
    def __init__(self, name: str):
        self.name = name
        self.pos = 1

class Dice:
    def __init__(self, _min_num: int, _max_num: int):
        self.min_num = _min_num
        self.max_num = _max_num
    
    def roll(self) -> int:
        return random.randint(self.min_num,self.max_num)