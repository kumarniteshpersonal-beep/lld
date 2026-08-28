from enum import Enum

class RequestEnum(Enum):
    PICK_UP = "PICK_UP"
    PICK_DOWN = "PICK_DOWN"
    DESTINATION = "DESTINATION"

class Request:
    def __init__(self, stop_floor: int, type: RequestEnum):
        self.stop_floor = stop_floor
        self.request_type = type

    def __hash__(self):
        return hash((self.stop_floor, self.request_type.value))
    
    # along with hash, eq is also needed
    def __eq__(self, other):
        if not isinstance(other, Request):
            return NotImplemented
        return self.stop_floor == other.stop_floor and self.request_type == other.request_type
    
    def __repr__(self):
        return str((self.stop_floor, self.request_type.value))