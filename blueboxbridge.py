from enum import Enum
import time

SLEEPTIME = 2



class STATES(Enum):
    CONNECTED = 1
    DISCONNECTED = 2
    NONE = 3

class Device():
    State = None
    DEVPATH = ""

    def __init__(self, DevPath_ : str):
        self.DEVPATH = DevPath_
        self.detectChange()

    def detectChange(self): # Checks if the device has a valid serial device TODO
        found = False
        return
        # if self.DEVPATH file exists -> found = true

        if found:
           self.State = STATES.CONNECTED
           return
        self.State = STATES.DISCONNECTED
        return
        
def copySerial(computer: Device, vexBrain: Device): # TODO
    print("Starting copySerial()")
    run = True
    emptyMessage = "".encode("ascii")
    print(emptyMessage)
    while run:

        # Open serial port vex brain -> brainSerial
        # Open Serial port computer -> compSerial

        # Read brainSerial
        # if(mes == emptyMessage):
        #   Write message to compSerial

        #
        break


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
    if( devList[0].State == STATES.CONNECTED and devList[1].State == STATES.CONNECTED ): # If both devices are connected
        print("Running Condition Met")
        copySerial(computer=computer, vexBrain=vexBrain) # run copying program
    else:
        print("Running Condition Failed, going to sleep")

    time.sleep(SLEEPTIME) #Delay 
    break