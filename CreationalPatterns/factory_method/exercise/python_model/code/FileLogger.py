from Logger import Logger
from FileUtil import FileUtil

class FileLogger(Logger):
    def log(self, msg):
        futil = FileUtil()
        futil.writeToFile("log.txt",msg,True,True)
