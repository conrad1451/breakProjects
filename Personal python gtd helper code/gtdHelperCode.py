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
  
def stringifyCalEvent(aCalEvent):
    line1 = "name: " + aCalEvent.theName + "\n"
    line2 = "day of week: " + aCalEvent.theDayOfWeek + "\n"
    line3 = "start time: " + str(aCalEvent.theStartTime) + "\n"
    line4 = "end time: " + str(aCalEvent.theEndTime) + "\n"
    line5 = "repeating event?: " + str(aCalEvent.theRepeat) + "\n"
    
    return line1 + line2 + line3 + line4 + line5


 
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
        
            theList.append(theStr[startPos : endPos+1])
            startPos = endPos + 1

    # end of while loop, last step is to return from function

    print("shown following for testing purposes", theList[2], "\n\n")
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
    
    name = stringList[0]
    firstDateToSplit = stringList[1]
    secondDateToSplit = stringList[2]
    
    #print("shown following for testing purposes", inputStr, "\n\n")
    
    if(stringList.len() > 0):
    {
        if (foundInText(firstDateToSplit, "2021"))
        {
            firstTimeSplitPos = firstDateToSplit.find("2021");
            theDay = firstDateToSplit.substr(0, firstTimeSplitPos - 1);
            stringifiedBeginTime = firstDateToSplit.substr(firstTimeSplitPos);

            beginTime = std::stoi(stringifiedBeginTime);
        }
        else
        {
            # I’m not processing dates before Jan 1 2021. Too hard.
        }


        if (foundInText(secondDateToSplit, "2021")) {
            secondTimeSplitPos = firstDateToSplit.find("2021");
            #  theDay = secondDateToSplit.substr(0, secondTimeSplitPos-1);
            stringifiedEndTime = secondDateToSplit.substr(secondTimeSplitPos);

            endTime = std::stoi(stringifiedEndTime);
        }
        else
        {
            # I’m not processing dates before Jan 1 2021. Too hard.
        }

        # call function grabDay in here to grab day of week and store in day
        #Following C++ code concerning time is limited to C++20, which I am having trouble to download
        #- receive strings and transform them into date objects
        #- determine the difference in days between two date objects
        #- determine the day of the week of a particular date


        # call function grabTime in here  to grab time and store in beginTime or endTime

        # Function grab time makes two substrings (one on each side of the colon) and
        # converts those substrings into size_t (using int to size_t casting if necessary)
        # before doing the math to store as a 3 or 4 dig number representing time
        # (like how you did it for app inventor)
     }
    
    testCalEvent = CalEvent(name, theDay.lower(), beginTime, endTime, False)
    return testCalEvent;





def autoConverter():
    fin = "";
    line = "";

    autoAddedCalEvents = []

    fin = input("Enter name of the input text file (should end in .csv): ")

    while (not foundInText(fin, ".csv")):
        fin = input("text file must end in .csv: ")
    

    fin = "inputFiles/" + fin

    # open input file to read content
    infile = open(fin, 'r')
    fileContent = infile.readlines()
    
    listOfLines = []
    for line in fileContent:
        if(line[-1] == '\n'):
            listOfLines.append(line[:-1])
        else:
            listOfLines.append(line)
            
    
    counter = 0
    
    for line in listOfLines:
        if(foundInText(line, ',') and not foundInText(line.lower(), "summary")):
        
            anEvent = automaticEventCreation(line)
            
            #print("Event #", str(counter), ": \n", stringifyCalEvent(anEvent), "\n\n")

            autoAddedCalEvents.append(anEvent)
            
            counter = counter + 1



def main():
    #myStr = "";
    allCalEvents = []
        
    anInput = input("Select 1 for the manual event scanning or 2 for the automatic event scanning): ")

    while(anInput != "1" and anInput != "2"):
        anInput = input("Select a valid input! (1 for the manual event scanning or 2 for the automatic event scanning): ")

    if(anInput == "1"):
        theCondition = True
        while (theCondition):
            allCalEvents.append(manualEventCreation())
            
            myStr = input("\nwant to add new event (Y|N): ")
            print("\n\n\n")
            theCondition = lower(myStr[0]) == 'y'

    elif (anInput == "2"):
        autoConverter()



main()

