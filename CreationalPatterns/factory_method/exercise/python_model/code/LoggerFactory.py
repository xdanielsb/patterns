from ConsoleLogger import ConsoleLogger
from FileLogger import FileLogger

class LoggerFactory:
    def isFileLoggingEnabled(self):
        try:
            p = __import__('.fileproperties', fromlist=["FileLogging"])
            fileLogginValue = p.FileLogging
            if fileLogginValue == "ON": return True
            else: return False
        except ModuleNotFoundError as detail:
            return False

    #Factory method
    def getLogger(self):
        if self.isFileLoggingEnabled():
            return FileLogger()
        else:
            return ConsoleLogger()
