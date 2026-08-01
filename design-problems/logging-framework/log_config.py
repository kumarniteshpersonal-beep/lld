from log_level import LogLevelType

class LogConfig:
    def __init__(self):
        self.level: LogLevelType = LogLevelType.DEBUG
        self.excludes: list[str] = None
    
    def set_level(self,level: LogLevelType):
        self.level = level
        return self
    
    def set_excludes(self,excludes: list[str]):
        self.excludes = excludes
        return self