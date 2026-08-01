from logger import Logger
from log_config import LogConfig
from log_level import LogLevelType
from backend import ConsoleBackend, FileBackend
import time

class LoggerFrameworkDemo:
    @staticmethod
    def main():
        log_config: LogConfig = LogConfig().set_level(LogLevelType.INFO).set_excludes(["/health"]) # create log config
        logger: Logger = Logger(config=log_config) # create logger instance
        logger.add_backend(ConsoleBackend()) # add console backend
        logger.add_backend(FileBackend(file_path="app.log")) # add file backend

        # now we can log
        logger.info("server startup")
        logger.info("request: /health") # should not print
        logger.debug("user: nitesh kumar") # should not print
        logger.warning("package 'lol' is deprecated")

        time.sleep(1) # wait for 1 second
        # gracefully shutdown the logger and close all backends
        try:
            logger.shutdown()
        except Exception as e:
            print(f"Error shutting down logger: {e}")

if __name__=="__main__":
    LoggerFrameworkDemo.main()