from elevator_selection_strategy import ElevatorSelectionStrategy, DirectionAndRequesAwareStrategy
from request import RequestEnum, Request
from elevator import Elevator
from threading import Thread, Lock
import time

class ElevatorController:
    def __init__(self):
        self.selection_strategy: ElevatorSelectionStrategy = DirectionAndRequesAwareStrategy()
        self.floors = 0
        self.elevators = []
        self._lock = Lock()
        # step function simulation
        self._is_running = True
        self.consumer_thread = Thread(target=self._consumer)

    
    def set_selection_strategy(self, selection_strategy):
        self.selection_strategy = selection_strategy
    
    def set_elevators(self, cnt: int):
        self.elevators = [Elevator() for _ in range(cnt)]
    
    def set_floors(self, cnt: int):
        self.floors = cnt

    # allow hall calls only
    def request_elevator(self, curr_floor: int, type: RequestEnum) -> Elevator | None:
        if type == RequestEnum.DESTINATION:
            return None
        if curr_floor < 0 or curr_floor >= self.floors:   # also fixes missing lower-bound check
            return None
        with self._lock:
            request = Request(curr_floor, type)
            best = self.selection_strategy.select_elevator(self.elevators, request)
            if not best.add_request(request):     # you're currently ignoring add_request's return value!
                return None
            return best
    
    # support call from inside of elevator
    def request_stop(self, elevator: Elevator, stop_floor: int) -> bool:
        if stop_floor < 0 or stop_floor >= self.floors:
            return False
        with self._lock:
            request = Request(stop_floor,RequestEnum.DESTINATION)
            return elevator.add_request(request)

    # move all elevators to next step
    def step(self):
        with self._lock:
            for e in self.elevators:
                e.step()

    # run step functions
    def _consumer(self):
        while self._is_running:
            time.sleep(0.5)
            self.step()

    def start(self):
        self.consumer_thread.start()

    # stop the elevator system
    def stop(self):
        self._is_running = False
        self.consumer_thread.join()
    
