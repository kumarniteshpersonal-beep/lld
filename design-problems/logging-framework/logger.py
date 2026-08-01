from log_config import LogConfig
from backend import Backend
from log_level import LogLevelType
from log_message import LogMessage
from log_processor import LogLevelProcessor, LogFilterProcessor
from threading import Lock
from async_dispatcher import AsyncLogDispatcher

class Logger:
    _instance = None
    _initialized = False
    _lock = Lock()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, config: LogConfig):
        if Logger._initialized:
            return
        
        self.logger_config = config
        self.backends: list[Backend] = []

        # create processing chain
        log_level_processor = LogLevelProcessor(config)
        log_filter_processor = LogFilterProcessor(config)
        log_level_processor.set_next_handler(log_filter_processor)

        self.handler = log_level_processor
        self._dispatcher = AsyncLogDispatcher()
        Logger._initialized = True

    def add_backend(self, backend: Backend):
        self.backends.append(backend)
    
    def process(self, level: LogLevelType, message: str):
        message_obj = LogMessage(message,level)
        message_obj = self.handler.handle(message_obj) # process the message through the chain of processors

        if message_obj is None:
            # ignore this log message
            return

        # submit log to dispatcher
        self._dispatcher.submit(message_obj, self.backends)

    def info(self,message: str):
        self.process(LogLevelType.INFO, message)

    def debug(self,message: str):
        self.process(LogLevelType.DEBUG, message)
    
    def warning(self,message: str):
        self.process(LogLevelType.WARNING, message)
    
    def error(self,message: str):
        self.process(LogLevelType.ERROR, message)
    
    def fatal(self,message: str):
        self.process(LogLevelType.FATAL, message)
    
    def shutdown(self):
        try:
            print("Shutting down logger...")
            # stop the dispatcher
            self._dispatcher.stop()
            # close all backends
            for backend in self.backends:
                backend.close()
        except Exception as e:
            print(f"Error during logger shutdown: {e}")
