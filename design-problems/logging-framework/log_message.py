from datetime import datetime
from log_level import LogLevelType

class LogMessage:
    def __init__(self, message: str, level: LogLevelType):
        self.timestamp = datetime.now()
        self.level = level
        self.message = message