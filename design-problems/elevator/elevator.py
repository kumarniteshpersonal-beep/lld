from request import Request, RequestEnum
from enum import Enum
from queue import Queue

class Direction(Enum):
    UP = "UP"
    DOWN = "DOWN"
    IDLE = "IDLE"

class Elevator:
    def __init__(self):
        self.requests: set[Request] = set()
        self.current_floor = 0
        self.curr_direction = Direction.IDLE

    def get_curr_direction(self):
        return self.curr_direction

    def get_curr_floor(self):
        return self.current_floor
    
    def add_request(self, request: Request) -> bool:
        # duplicate req
        if request in self.requests:
            return False
        # if elevator already stopped at current floor
        if request.stop_floor==self.current_floor:
            return False
        # add to request set
        self.requests.add(request)
        print(f"request: {request} assigned to elevator: {self}")
        return True

    def _has_request_at_or_beyond(self,hall,requested_dir) -> bool:
        for _request in self.requests:
            # outer condition checks if any request passes this hall
            if requested_dir==Direction.UP and _request.stop_floor >= hall:
                # inner condition is that if that request is in same direction as request from hall
                if _request.request_type==RequestEnum.PICK_UP or _request.request_type==RequestEnum.DESTINATION:
                    return True
            elif requested_dir==Direction.DOWN and _request.stop_floor <= hall:
                if _request.request_type==RequestEnum.PICK_DOWN or _request.request_type==RequestEnum.DESTINATION:
                    return True
        return False

    def _any_request_in_curr_direction(self) -> bool:
        for request in self.requests:
            if self.curr_direction==Direction.UP:
                if request.stop_floor > self.current_floor:
                    return True
            else:
                if request.stop_floor < self.current_floor:
                    return True
        return False

    def step(self):
        # no request to fulfil
        if not self.requests:
            self.curr_direction = Direction.IDLE
            return
        # if elevator is idle and some request come we will set the direction of nearest request
        if self.curr_direction==Direction.IDLE:
            nearest_stop = None
            for request in self.requests:
                if nearest_stop is None:
                    nearest_stop = request
                else:
                    if abs(nearest_stop.stop_floor - self.current_floor) > abs(request.stop_floor - self.current_floor):
                        nearest_stop = request
            self.curr_direction = Direction.UP if nearest_stop.stop_floor > self.current_floor else Direction.DOWN
        # should we stop at current floor if yes then we have to open the door without moving elevator
        # we are follwing disk-scheduling SCAN algo hence we will only entertain request which are in curr direction
        hall_call_request = Request(self.current_floor, RequestEnum.PICK_UP if self.curr_direction==Direction.UP else RequestEnum.PICK_DOWN)
        internal_call_request = Request(self.current_floor, RequestEnum.DESTINATION)
        if hall_call_request in self.requests or internal_call_request in self.requests:
            # perform actions to open the door
            self.requests.discard(hall_call_request)
            self.requests.discard(internal_call_request)
            print(f"opening door of elevator: {self} at floor: {self.current_floor}")
            if not self.requests:
                self.curr_direction = Direction.IDLE
            return
        # do we need to continue in current direction or reverse
        if not self._any_request_in_curr_direction():
            self.curr_direction = Direction.UP if self.curr_direction==Direction.DOWN else Direction.DOWN
            return
        # finally move the elevator in current direction
        if self.curr_direction==Direction.UP:
            self.current_floor+=1
        elif self.curr_direction==Direction.DOWN:
            self.current_floor-=1
        print(f"setting current_floor to {self.current_floor} for elevator: {self}")
    
    def __repr__(self):
        return str(id(self))
