from datetime import datetime
 
 
# ---------------------- MY STANDARD HELPER FUNCTIONS -------------------- #

# returns true if 'theChar' is found in 'theStr'
def foundInText(theStr, theChar):
    # returns true if 'theChar' is found in 'str'
    return theStr.find(theChar) != -1;

# returns true if 'substr' is found in 'theStr'
def foundInText(theStr, substr):
    # returns true if 'substr' is found in 'str'
    return theStr.find(substr) != -1;

# note that all string methods return new values
# source: https://www.w3schools.com/python/python_ref_string.asp

# things that are standard in python library (but not C++)
# "==" to compare two strings to determine if their characters are equal
# casefold() to convert a string to lower case
# lower() to convert a string to lower case
# islower() to determine if all the characters in a stirng are lowercase
# isnumeric() to determine if all the characters in a string are numeric 
 
# ----------------------------------------------------------------------- # 
 
 
class CalEvent(object):
    name = ""
    age = 0
    major = ""
    
    
    theName = ""
    theDayOfWeek = ""
    theStartTime = 0
    theEndTime = 0
    theRepeat = False
    

    # The class "constructor" - It's actually an initializer 
    def __init__(self, theName, theDayOfWeek, theStartTime, theEndTime, theRepeat):
        self.theName = theName
        self.theDayOfWeek = theDayOfWeek
        self.theStartTime = theStartTime
        self.theEndTime = theEndTime
        self.theRepeat = theRepeat

def make_calEvent(theName, theDayOfWeek, theStartTime, theEndTime, theRepeat):
    calEvent = CalEvent(theName, theDayOfWeek, theStartTime, theEndTime, theRepeat)
    return calEvent
  

 
def elapsedTimeBetweenTwoDates(firstTime, secondTime):
    fTime = datetime.strptime(firstTime, '%m/%d/%Y')
    sTime = datetime.strptime(secondTime, '%m/%d/%Y')
    
    print("\n")
    
    print("the first time is: ", fTime)
    print("and the second time is: ", sTime)
    


def splitIntoStringList(theStr, charSplitter):
    # takes in a string called "theStr" and character called "theChar" and returns a list of strings
    
    theList = []
    startPos = 0
    endPos = 0

    while (foundInText(theStr, charSplitter) and endPos != -1):
    
        endPos = theStr.find(charSplitter, startPos)
        if (endPos != -1):
        
            theList.push_back(theStr.substr(startPos, endPos))
            startPos = endPos + 1

    # end of while loop, last step is to return from function

    return theList;
    
    

def automaticEventCreation(inputStr):
    # takes in a string called "inputStr" and returns a CalEvent
    stringList = splitIntoStringList(inputStr, ',')
    firstTimeSplitPos = 0
    secondTimeSplitPos = 0
    
    # FIXME
    theDay = ""
    stringifiedBeginTime = ""
    stringifiedEndTime = ""
    beginTime = 0
    endTime = 0
    
    name = stringList.at(0)
    firstDateToSplit = stringList.at(1)
    secondDateToSplit = stringList.at(2)
    
    testCalEvent = CalEvent(name, lowerCaseString(theDay), beginTime, endTime, false)
    return testCalEvent;





def autoConverter():
    fin = "";
    line = "";

    autoAddedCalEvents = []

    fin = input("Enter name of the input text file (should end in .csv): ")

    while (not foundInText(fin, ".csv")):
        fin = input("text file must end in .csv: ")
    

    fin = "inputFiles/" + fin

    # open input file
    infile = open(fin, 'r')
    fileContent = infile.readlines()
    
    listOfLines = []
    for line in fileContent:
        if(line[-1] == ‘\n’):
            listOfLines.append(line[:-1])
        else:
            listOfLines.append(line)
    
    for line in listOfLines:
        if(foundInText(line, ',') and !foundInText(lower(line), "summary")):
        
            anEvent = automaticEventCreation(line)

            autoAddedCalEvents.push_back(anEvent)

    closeInputFile(infile);




    
a = input("enter first time: ")
b = input("enter second time: ")


elapsedTimeBetweenTwoDates(a, b)
