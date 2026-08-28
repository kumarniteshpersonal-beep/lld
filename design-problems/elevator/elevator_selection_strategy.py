from abc import ABC, abstractmethod
from elevator import Elevator, Direction
from request import Request, RequestEnum

class ElevatorSelectionStrategy(ABC):
    @abstractmethod
    def select_elevator(self, elevators: list[Elevator], request: Request) -> Elevator:
        pass

class NearestStrategy(ElevatorSelectionStrategy):
    def select_elevator(self, elevators: list[Elevator], request: Request) -> Elevator:
        # assign req to elevator which is nearest to the hall
        pass

class DirectionAwareStrategy(ElevatorSelectionStrategy):
    def select_elevator(self, elevators: list[Elevator], request: Request) -> Elevator:
        # the elevator which is coming towards the hall
        # if nothing like that choose nearest but idle elevators
        # if nothing like that choose nearest
        pass

class DirectionAndRequesAwareStrategy(ElevatorSelectionStrategy):
    def _find_elevator_moving_toward_hall(self, elevators: list[Elevator], request: Request):
        requested_dir = Direction.DOWN if request.request_type==RequestEnum.PICK_DOWN else Direction.UP
        hall = request.stop_floor
        nearest = None
        for elevator in elevators:
            if requested_dir!=elevator.curr_direction:
                continue
            # here we are not only checking the moving towards elevators but also the one who has some request which will pass or stop at requested hall
            if not elevator._has_request_at_or_beyond(hall,requested_dir):
                continue
            if elevator.curr_direction==Direction.UP and hall > elevator.current_floor or elevator.curr_direction==Direction.DOWN and hall < elevator.current_floor:
                if nearest is None:
                    nearest = elevator
                else:
                    if abs(nearest.current_floor - hall) > abs(elevator.current_floor - hall):
                        nearest = elevator
        return nearest

    def _nearest_idle(self, elevators: list[Elevator], request: Request):
        hall = request.stop_floor
        nearest = None

        for elevator in elevators:
            if elevator.curr_direction!=Direction.IDLE:
                continue
            if nearest is None:
                nearest = elevator
            else:
                if abs(nearest.current_floor - hall) > abs(elevator.current_floor - hall):
                    nearest = elevator
                
        return nearest

    def _nearest(self, elevators: list[Elevator], request: Request):
        hall = request.stop_floor
        nearest = None

        for elevator in elevators:
            if nearest is None:
                nearest = elevator
            else:
                if abs(nearest.current_floor - hall) > abs(elevator.current_floor - hall):
                    nearest = elevator
                
        return nearest

    def select_elevator(self, elevators: list[Elevator], request: Request) -> Elevator:
        best = self._find_elevator_moving_toward_hall(elevators,request)
        if best:
            return best
        
        best = self._nearest_idle(elevators, request)
        if best:
            return best

        best = self._nearest(elevators,request)
        if best:
            return best