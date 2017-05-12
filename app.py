import ScanRFID
from TogglPy import Toggl
import json
from time import sleep

toggl = Toggl()
toggl.setAPIKey("")

def autoScan():
    """ 
    This function loops the RFID scanning function and returns UID of
    RFID card. It is polling and sleeping the program at 1 sec intervals.
    """
    while True:
        card = ScanRFID.getSerial()
        if card != 0:
            return card
        else: 
            sleep(1)

def lookupCards(UID):
    """
    Looks up the Unique ID of the RFID card in the cards.json file in the
    program directory. Throws a KeyError if card is not registered.
    """
    print "Looking up card in json file..."
    try:
        with open('./cards.json') as cardsFile:
            cards = json.load(cardsFile)
            togglprojectid = cards["cards"][UID]
            if togglprojectid:
                return togglprojectid
    except KeyError as e:
        print "Card is not registered, KeyError thrown"
        return
    except:
        print "An error in looking up json occured"
        return

def stopCurrentTimer():
    currentTimer = toggl.currentRunningTimeEntry()
    toggl.stopTimeEntry(currentTimer['data']['id'])
    return "timer stopped"

def newTimer(myprojectpid):
    """ Sets a new timer in Toggl"""
    stopCurrentTimer()
    if myprojectpid != "HALT ALL":
        print "starting new timer!"
        toggl.startTimeEntry("Automatic punchin at NSP", myprojectpid)
    else:
        print "Timers stopped"

if __name__ == "__main__":
    print "program initiated!"
    while True:
        card = autoScan()
        projectid = lookupCards(card)
        if projectid:
            newTimer(projectid)