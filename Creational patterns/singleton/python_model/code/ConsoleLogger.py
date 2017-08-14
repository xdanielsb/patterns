from Logger import Logger
class ConsoleLogger(Logger):
    def log(self, msg):
        print(msg)
