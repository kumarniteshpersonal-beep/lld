from abc import ABC, abstractmethod
from log_message import LogMessage

class LogFormatter(ABC):
    @abstractmethod
    def format(self):
        pass

class TextFormatter(LogFormatter):
    def format(self, message: LogMessage):
        return f"{message.timestamp} - {message.level.name}: {message.message}"

class JSONFormatter(LogFormatter):
    def format(self, message: LogMessage):
        return {
            "timestamp": str(message.timestamp),
            "level": message.level.name,
            "message": message.message
        }