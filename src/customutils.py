from models import Route

DEBUG_MODE = True

def cleanup(text_array):
    # Remove Some WhiteSpaces
    for i in text_array:
        if (i == "" or i == "\n" or i == " " or i == "\s" ):
            text_array.remove(i)
    return text_array

def PageCreation(text_array):
    # Main Method that handles route creation
    FirstRoute = True
    StartLocation = ""
    EndLocation = ""
    RouteName = ""
    RouteProvider = ""
    RouteList = []
    text_array.remove(text_array[0])
    StartLocation = LocationParsing(text_array)
    EndLocation = LocationParsing(text_array)
    RouteName = text_array[0]
    text_array.remove(text_array[0])

    if "Including" in text_array[0]:
        text_array.remove(text_array[0])
        text_array.remove(text_array[0])
        text_array.remove(text_array[0])

    RouteProvider = text_array[0]
    text_array.remove(text_array[0])
    if DEBUG_MODE:
        print("Start Location: " + StartLocation)
        print("End Location: " + EndLocation)
        print("RouteName: " + RouteName)
        print("RouteProvider: " + RouteProvider)
    DeleteUntilAnchor(text_array,StartLocation,True)
    StartLocationTimes = TimeExtraction(text_array)
    TimeExtractionSetup(text_array)
    EndLocationTimes = TimeExtraction(text_array)
    TimeExtractionSetup(text_array)
    Departure1Times = TimeExtraction(text_array)
    DirectionSetup(text_array)
    Direction1Times = DirectionTimeExtraction(text_array)
    TimeExtractionSetup(text_array)
    Departure2Times = TimeExtraction(text_array)
    DirectionSetup(text_array)
    Direction2Times = DirectionTimeExtraction(text_array)
    DeleteUntilAnchor(text_array,0,False)
    RouteList = RouteParsing(text_array)
    
    
    
    
def RouteParsing(text_array):
    
    RouteList = []
    route = {
        "Fare_stage":0,
        "Locality":LocationParsing(text_array),
        "avgjourn":0,
        "Fare_stage2":0,
        "Locality2":LocationParsing(text_array),
        "avgjourn2":0
    }
    RouteList.append(route)
    return RouteList
    

def LocationParsing(text_array):
    if (DEBUG_MODE):
        print("Location Parsing ")
    # Early Cleaning In some cases
    location = ""
    if hasNumbers(text_array[0]):
        text_array.remove(text_array[0])
    if text_array[0] == "-":
        text_array.remove(text_array[0])

    if len(text_array[0]) < 2:
        location += text_array[0]
        text_array.remove(text_array[0])

    # Different Methods for Extracting Locations from NTA Bus Route Files
    if ("-" in text_array[1] or "(" in text_array[1]) and text_array[1].startswith("(") is False:
        if DEBUG_MODE:
            print("method1")
        location = text_array[0]
        text_array.remove(text_array[0])

    elif "(" in text_array[0]:
        if DEBUG_MODE:
            print("method2")
        while ")" not in text_array[0]:
            location += text_array[0] + " "
            text_array.remove(text_array[0])
        location += text_array[0]
        text_array.remove(text_array[0])

    else:
        if DEBUG_MODE:
            print("default method")
        location = text_array[0] + " " + text_array[1]
        text_array.remove(text_array[0])
        text_array.remove(text_array[0])
    
    # Capture Via exception
    if text_array[0].lower().startswith("via"):
        location += " " + text_array[0]
        text_array.remove(text_array[0])

    if (DEBUG_MODE):
        print ("result location : "+ location+'\n')
    return location

def DeleteUntilAnchor(text_array,anchor,bDeleteAnchor):
        # Will Delete Text Array 0 anchor inclusive
        # until reaches anchor value
        anchor = str(anchor)
        while text_array[0].lower() not in anchor.lower():
            text_array.remove(text_array[0])
        if bDeleteAnchor:
            text_array.remove(text_array[0])


def TimeExtraction(text_array):
    # Extract Times 
    TimeArray=[]
    while hasNumbers(text_array[0]) and ("direction" in text_array[0].lower()) is False:
        TimeArray.append(text_array[0])
        text_array.remove(text_array[0])
    return TimeArray
def TimeExtractionSetup(text_array):
    # Setup By Removing Non-Digit Containing Elements
    while (hasNumbers(text_array[0]) is False):
        text_array.remove(text_array[0])

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

def DirectionTimeExtraction(text_array):
    TimeArray = []
    temp = ""
    while (("departure" in text_array[0].lower()) is False) and (("direction" in text_array[0].lower()) is False):
        if ("minutes" in text_array[0]):
            temp += text_array[0] + " "
            text_array.remove(text_array[0])
            TimeArray.append(temp)
            temp = ""
        else:
            temp += text_array[0]
            text_array.remove(text_array[0])
    return TimeArray


def DirectionSetup(text_array):
    while "direction" in text_array[0].lower():
        text_array.remove(text_array[0])