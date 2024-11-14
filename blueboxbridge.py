from enum import Enum
import time

class STATES(Enum):
    CONNECTED = 1
    DISCONNECTED = 2
    NONE = 3

class Device():
    State = None
    DEVPATH = ""

    def __init__(self, DevPath_ : str):
        self.DEVPATH = DevPath_
        self.State = STATES.NONE
        self.detectChange()

    def detectChange(self): # Checks if the device has a valid serial device
        found = False

        # if self.DEVPATH file exists -> found = true

        if found:
           self.State = STATES.CONNECTED
           return
        self.State = STATES.DISCONNECTED
        return
        
def copySerial(devList: list[Device]):
    print("Starting copySerial()")
    run = True
    while run:
        pass
        






computer = Device(DevPath_ = "/dev/rfcomm0" )
vexBrain = Device(DevPath_ = "" )

computer.State = STATES.CONNECTED
vexBrain.State = STATES.CONNECTED


devList = [computer, vexBrain]

while True:

    print("Updating devList States")
    for dev in devList: # Updates the state of the connection for each device
        dev.detectChange()

    print("Checking Run Condition")
    if( devList[0].State == STATES.CONNECTED and devList[1].State == STATES.CONNECTED ):
        copySerial(devList)
        # run copying program

    time.sleep(3) #Delay 




    break