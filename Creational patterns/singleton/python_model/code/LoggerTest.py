from LoggerFactory import LoggerFactory
import sys


class LoggerTest:

    @staticmethod
    def main(args):
        factory = LoggerFactory()
        logger = factory.getLogger()
        logger.log("A Message to Log")

if __name__ == "__main__":
    LoggerTest.main(sys.argv)
