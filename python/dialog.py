# Version
# Date 12.12.2018

# Imports

# Global Variables
#
#
#
DEBUG = False


# Functions

# method-type: get
# function returns open file
#
def openFile(filename, filepath):
    if len(filename) <= 0:
        raise ValueError("filename length cant be lower equals zero")
    if ".txt" not in filename:
        raise ValueError("filename should end on .txt")
    #TODO: Add more types then .txt
    try:
        dialogFile = open(filepath+"/"+filename, 'r')
    except IOError as e:
        print("Cannot open filename: " + filepath + "/" + filename)
        raise IOError("Unable to open file")

    if DEBUG:
        print("dialogFile: ")
        print(dialogFile)

    return dialogFile

#
#
#
def closeFile(fileObject):
    #TODO check if file is fileObject
    fileObject.close()

#
# Dialog Class
# Python Interface for Dialog Script
class Dialog:

    def __init__(self, filename, filepath):
        # Init Dialog
        self.counter = -1 # Internal counter where the dialog is
        self.end = False # Boolean if the end of the dialog is reached

        self.choice = False # Boolean if theres an active choice
        self.choices = [] # Array with all choices

        # Get Content of the dialog file
        dialogFile = openFile(filename, filepath)
        self.dialogScript = dialogFile.readlines() # Variable with all the dialog content
        closeFile(dialogFile)

        #TODO: check syntax
        self.currentLine = ""
        self.update()

        self.speaker = self.findFirstSpeaker() # the current speaker

    # ==== Public Functions ====

    #
    # method-type: get
    # Returns the current Speaker
    def getSpeaker(self):
        return self.speaker

    #
    # method-type: get
    # Returns if the end of the dialog is reached
    def ending(self):
        return self.end

    #
    # method-type: get
    # Returns if a choice is reached in dialog
    def choosing(self):
        return self.choice

    #
    #
    #
    def update(self):
        # Check if end is reached
        if (self.counter + 1) >= len(self.dialogScript):
            self.end = True
            return

        # Raise counter and prepare next line
        self.counter += 1
        line = self.dialogScript[self.counter]

        line = self.cleanUpLine(line)

        # Check if line is empty
        if line == "":
            self.update()
            return

        # Check for Keywords
        if self.isSpeaker(line):
            self.speaker = self.getSpeakerFromLine(line)
            self.update()
            return

        if self.isGoto(line):
            self.goto(line)
            return

        if(self.isLabel(line)):
            self.update()
            return

        # Check if line is last line
        if (self.counter + 1) >= len(self.dialogScript):
            self.end = True
        else:
            nextLine = self.dialogScript[self.counter + 1]
            # Check if next line is end
            if self.isEnd(nextLine):
                self.end = True

        self.currentLine = line

    #
    # method-type: get
    #
    def nextText(self):

        # Get current line
        line = self.currentLine
        return self.getText(line)

    # ==== Private Functions ====

    #
    # method-type: get
    # Returns the first speaker
    def findFirstSpeaker(self):
        for line in self.dialogScript:
            if self.isSpeaker(line):
                return self.getSpeakerFromLine(line)
        return ""

    #
    #   method-type: get
    #
    def getText(self, line):
        return line.replace('"' , "")

    #
    #   method-type: get
    #
    def getSpeakerFromLine(self, line):
        # speaker Emily+Erdbeer -> Emily Erdbeer
        return line.replace(" ", "")[line.replace(" ", "").find("speaker")+7:].replace("+", " ").replace("\n", "")

    #
    # method-type: boolean-query
    #
    def isSpeaker(self, line):
        if line.replace(" ", "").find("speaker") == 0:
            return True
        else:
            return False

    #
    #
    #
    def getLabelFromLine(self, line):
        # label LabelName: -> LabelName
        return line.replace(" ", "")[line.replace(" ", "").find("label")+4:].replace("\n", "")

    #
    # method-type: boolean-query
    #
    def isLabel(self, line):
        if line.replace(" ", "").find("label") == 0:
            return True
        else:
            return False

    #
    # method-type: boolean-query
    #
    def isGoto(self, line):
        if line.replace(" ", "").find("goto") == 0:
            return True
        else:
            return False

    #
    # method-type: boolean-query
    #
    def isEnd(self, line):
        if line.find("end") == 0:
            return True
        else:
            return False

    #
    # TODO make this function better
    #
    def goto(self, line):
        to = line.replace(" ", "")[line.replace(" ", "").find("goto")+4:].replace("\n", "")
        if to.isdigit():
            lineIndex = int(to)
            if lineIndex < len(self.dialogScript):
                self.counter = lineIndex-2
            else:
                self.counter = len(self.dialogScript)-1
                self.end = True
        else:
            c = 0
            for line in self.dialogScript:
                if self.isLabel(line) and to in self.getLabelFromLine(line):
                    self.counter = c
                    break
                c += 1
        self.update()

    #
    # method-type: modify
    #
    def cleanUpLine(self, line):
        return self.removeMeta(self.removeComment(line.lstrip())).replace("\n", "")

    #
    # method-type: modify
    # Removes comment from a line
    def removeComment(self, line):
        #TODO Check if // is in "Wow cooler Dialog mit diesem Zeichen // in sich"
        if line.find("//") != -1:
            return line[:line.find("//")]
        else:
            return line

    #
    # method-type: modify
    # Removes meta information from a line
    def removeMeta(self, line):
        if line.find("meta") == 0:
            return ""
        else:
            return line
