from ScanRFID import getSerial
from TogglPy import Toggl
import json

def autoScan():
    print getSerial

def stopCurrentTimer():
    currentTimer = toggl.currentRunningTimeEntry()
    toggl.stopTimeEntry(currentTimer['data']['id'])
    return "timer stopped"

def newTimer():
    print "starting new timer!"
    myprojectpid = ****
    toggl.startTimeEntry("Automatic punchin at NSP", myprojectpid)

if __name__ == "__main__":
    print "program initiated!"
    toggl = Toggl()
    toggl.setAPIKey("APIKEY")
    newTimer()
