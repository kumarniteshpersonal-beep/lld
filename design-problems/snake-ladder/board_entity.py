from abc import ABC

class BoardEntity(ABC):
    def __init__(self, _start: int, _end: int):
        self.start = _start
        self.end = _end

class Snake(BoardEntity):
    pass

class Ladder(BoardEntity):
    pass