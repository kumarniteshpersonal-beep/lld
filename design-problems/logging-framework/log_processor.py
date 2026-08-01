from abc import ABC, abstractmethod
from log_config import LogConfig
from log_message import LogMessage

class LogProcessor(ABC):
    def __init__(self, config: LogConfig):
        self.log_config = config
        self.next_handler = None
    
    def set_next_handler(self, next_handler: 'LogProcessor'):
        self.next_handler = next_handler
        return self

    @abstractmethod
    def handle(self, message: LogMessage):
        pass

    def next(self, message: LogMessage):
        if self.next_handler:
            return self.next_handler.handle(message)
        return message

class LogLevelProcessor(LogProcessor):
    def handle(self, message: LogMessage):
        curr_log_level = message.level
        if curr_log_level.value >= self.log_config.level.value:
            return self.next(message)
        return None


class LogFilterProcessor(LogProcessor):
    def handle(self, message: LogMessage):
        excludes = self.log_config.excludes
        content = message.message
        if not any([keyword in content for keyword in excludes]):
            return self.next(message)
        return None
