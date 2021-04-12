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

    # TODO
    #print("shown following for testing purposes", theList[2], "\n\n")
    return theList;




def grabDay(myStringifiedDate):
    commaPos = myStringifiedDate.find(",")
    
    return myStringifiedDate[commaPos-3 : commaPos]
    
    
    
    
def grabTime(dateToSplit):
    timeSplitPos = dateToSplit.find("2021")
    stringifiedTime = dateToSplit[timeSplitPos + 5: -4]
    
    theHr = stringifiedTime[0 : -3]
    theMin = stringifiedTime[-2 :]
    
    return int(theHr)*100 + int(theMin)
    



def automaticEventCreation(inputStr):
    # takes in a string called "inputStr" and returns a CalEvent
    
    # lets make following assumptions
    # every event is contained within a single day (as opposed to spanning days)
    stringList = splitIntoStringList(inputStr, ',')
    firstTimeSplitPos = 0
    secondTimeSplitPos = 0
    
    # FIXME
    dayOfWeek = ""
    stringifiedBeginTime = ""
    stringifiedEndTime = ""
    beginTime = 0
    endTime = 0
    
    dayOfWeek = ""
    
    name = stringList[0]
    firstDateToSplit = stringList[1]
    secondDateToSplit = stringList[2]

    # TODO - test done
    #print("shown following for testing purposes", inputStr, "\n\n")
    
    if(len(stringList) > 0):
        if (foundInText(firstDateToSplit, "2021")):
            
            firstTimeSplitPos = firstDateToSplit.find("2021")
            beginTime = grabTime(firstDateToSplit)
            
            theDay = firstDateToSplit[0 : firstTimeSplitPos + 4]

            timeFormattedDate = datetime.strptime(theDay, '%m/%d/%Y')
            stringFormattedDate = timeFormattedDate.strftime('%a,  %m/%d/%Y %H:%M:%S')
            
            # TODO - test done
            # print("Date in dd/mm/yyy format: ", stringFormattedDate)
            
            dayOfWeek = grabDay(stringFormattedDate)
            
            print("Day of week: ", dayOfWeek)
            # TODO - test done
            print("begin time: ", beginTime)

        #else:
            # I’m not processing dates before Jan 1 2021. Too hard.


        if (foundInText(secondDateToSplit, "2021")):
            
            secondTimeSplitPos = secondDateToSplit.find("2021")
            endTime = grabTime(secondDateToSplit)
            # TODO - test done
            print("end time: ", endTime, "\n\n")

        #else
            # I’m not processing dates before Jan 1 2021. Too hard.

         
     
    testCalEvent = CalEvent(name, dayOfWeek.lower(), beginTime, endTime, False)
    return testCalEvent;





def autoConverter():
    fin = "";
    line = "";

    autoAddedCalEvents = []

    fin = input("Enter name of the input text file (should end in .csv): ")

    while (not foundInText(fin, ".csv")):
        fin = input("text file must end in .csv: ")
    
    print("\n")

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
            # FIXME: Add manualEventCreation as a function
            #allCalEvents.append(manualEventCreation())
            
            myStr = input("\nwant to add new event (Y|N): ")
            print("\n\n\n")
            theCondition = (myStr.lower())[0] == 'y'

    elif (anInput == "2"):
        autoConverter()



main()

