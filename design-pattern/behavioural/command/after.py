# reciever class
class TV:
    def turn_on(self):
        print("TV ON")

    def turn_off(self):
        print("TV OFF")

# command interface
class Command:
    def execute(self):
        pass

# concrete command classes that implement the Command interface and call the appropriate methods on the TV receiver
class TurnOnCommand(Command):
    def __init__(self, tv: TV):
        self.tv = tv

    def execute(self):
        self.tv.turn_on()

class TurnOffCommand(Command):
    def __init__(self, tv: TV):
        self.tv = tv

    def execute(self):
        self.tv.turn_off()

# invoker class that holds a reference to a Command object and calls its execute method when the button is pressed
class Remote:
    def __init__(self):
        self.command = None

    def set_command(self, command: Command):
        self.command = command

    def press_button(self):
        if self.command:
            self.command.execute()

# client code
tv = TV()
turn_on_command = TurnOnCommand(tv)
turn_off_command = TurnOffCommand(tv)

remote = Remote()
remote.set_command(turn_on_command)
remote.press_button()  # TV ON
remote.set_command(turn_off_command)
remote.press_button()  # TV OFF


# Core idea is that command is the one which has reciever api info and invoker has command reference and client is responsible for creating command and setting it to invoker. 
# This way we can decouple invoker from reciever and we can add new commands without modifying the invoker. We can also add new recievers without modifying the commands. This follows the Open/Closed Principle. 