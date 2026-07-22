# before
class Logger:
    def __init__(self):
        self.logs = []
    
    def log(self, message):
        self.logs.append(message)
        print(f"Log: {message}")

# client code
print(Logger() is Logger())  # False, different instances


# after
class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.logs = []

    def log(self, message):
        self.logs.append(message)
        print(f"Log: {message}")

print(Logger() is Logger())  # True, same instances

# problems:
# 1. Above implementation is only creating a single instance of Logger class, but it is not thread-safe.

# after (thread-safe)
import threading

class Logger:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:  # double-checked locking
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.logs = []

    def log(self, message):
        self.logs.append(message)
        print(f"Log: {message}")

print(Logger() is Logger())  # True, same instances
