from abc import ABC, abstractmethod
from log_formatter import LogFormatter, TextFormatter, JSONFormatter
from log_message import LogMessage
import json
from threading import Lock

class Backend(ABC):
    def __init__(self):
        self.formatter: LogFormatter = None
    
    @abstractmethod
    def _write(self, message: LogMessage):
        pass

    @abstractmethod
    def close(self):
        pass

class ConsoleBackend(Backend):
    def __init__(self):
        self.formatter: LogFormatter = TextFormatter()
    
    def _write(self, message: LogMessage):
        formatted_msg = self.formatter.format(message)
        print(formatted_msg)
    
    def close(self):
        pass

class FileBackend(Backend):
    def __init__(self, file_path: str):
        self.formatter: LogFormatter = JSONFormatter()
        self._lock = Lock()
        try:
            self.writer = open(file_path, 'a')
        except Exception as e:
            print(f"Error opening file {file_path}: {e}")
            self.writer = None

    def _write(self, message: LogMessage):
        formatted_msg = self.formatter.format(message)
        # acquire lock to ensure that multiple threads do not write to the file simultaneously
        with self._lock:
            if self.writer:
                try:
                    self.writer.write(json.dumps(formatted_msg) + "\n")
                    self.writer.flush()
                except Exception as e:
                    print(f"Failed to write logs to file, exception: {e}")

    def close(self):
                # acquire the same lock used by _write() so shutdown cannot
                # close the file while another thread is writing.
                with self._lock:
                    if self.writer:
                        try:
                            self.writer.close()
                        except Exception as e:
                            print(f"Failed to close the file writer, exception: {e}")
                        finally:
                            self.writer = None