class FileUtil:

    def writeToFile( self, fileName,  dataLine,  isAppendMode,  isNewLine):
        mode = "w"
        if (isNewLine):
            dataLine = "\n" + dataLine
        if (isAppendMode):
            mode = "a"
        try:
            outFile = open(fileName, mode)
            outFile.write(dataLine)
            outFile.close()
        except FileNotFoundError as detail:
            return False
        return True
