from Logger import Logger
from FileUtil import FileUtil
import threading
import functools

def synchronized(wrapped):
    lock = threading.Lock()
    @functools.wraps(wrapped)
    def _wrap(*args, **kwargs):
        with lock:
            return wrapped(*args, **kwargs)
    return _wrap

class FileLogger(Logger):

    __logger = None

    def __init__(self):
        """ Private constructor. """
        if FileLogger.__logger != None:
            raise Exception("This class is a singleton!")
        else:
            FileLogger.__logger = self

    @staticmethod
    def getFileLogger():
        """ Static access method. """
        if __logger == None:
            __logger = Singleton()
        return __logger

    @synchronized
    def log(self, msg):
        futil = FileUtil()
        futil.writeToFile("log.txt",msg,True,True)
