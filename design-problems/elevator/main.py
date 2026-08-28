from elevator_controller import ElevatorController
from request import RequestEnum
import time

class ElevatorDemo:
    @staticmethod
    def main():
        # system setup 
        controller = ElevatorController()
        controller.set_elevators(3)
        controller.set_floors(10)

        # start the controller which will move elevators using step function
        controller.start()

        # perform some hall calls
        el1 = controller.request_elevator(1,RequestEnum.PICK_UP)
        time.sleep(2)   # let a tick or two happen
        el2 = controller.request_elevator(2,RequestEnum.PICK_UP)
        time.sleep(2)   # let a tick or two happen
        el3 = controller.request_elevator(5, RequestEnum.PICK_DOWN)

        # click button from inside
        controller.request_stop(el1,6)
        controller.request_stop(el2,4)
        controller.request_stop(el3,2)

        # stop the elevators
        time.sleep(500)
        controller.stop()

ElevatorDemo.main()