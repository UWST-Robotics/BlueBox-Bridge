from fastapi import FastAPI
import os
from os import listdir
from os.path import isfile, join


app = FastAPI()

IP = "192.168.1.1"
PORT = 8100

YAMLHEADER = "%YAML 1.1\n---\n\n"

PORTS = [] # [ portNum, usbPath ]

# Helper Functions
def getSerialConfig(id: int, path: str) -> str: # Tested Working
    # Returns config for serial device to telnet
    res = "connection: &serialcon"+ str(id) +"\n  accepter: telnet,tcp, "+str(IP)+", "+str(PORT + id)+"\n  enable: on\n  connector: serialdev, "+path+", local\n\n"
    print(res)
    return res

def resetSer2NetService() -> str: # TESTED WORKING
    #run linux command to reset ser2net.service
    command = "systemctl restart ser2net"
    os.system(command)
    return "success"

def getSerialDevices() -> list[str]: #TESTED WORKING
    # Get list of serial devices in folder /dev/serial
    serialPath = "/dev/serial/by-id/"
    onlyfiles = os.listdir(serialPath)
    ret = []
    for x in onlyfiles:
        ret.append(serialPath + x)
    return ret

# System Functions
def systemWifiMode() -> str: # Tested Working
    #run linux command to reset ser2net.service
    command = "systemctl restart ser2net"
    os.system(command)
    return "success"

# Main Functions
@app.get("/")
def ping() :# Tested Working
    return {"status": "pong"}

@app.get("/ports")
def getPorts(): # Tested Working
    # Returns list of ports
    return {"ports": PORTS}

@app.get("/setPorts")
def setPorts():
     # Returns list of ports
    devs = getSerialDevices()

    # new yaml config
    f = open("/etc/ser2net.yaml", "w") # w will overwrite the existing file
    f.write(YAMLHEADER) # set YAMLHEADER

    for x in range(0, len(devs)): # Tetsed Working
        f.write(getSerialConfig(x,devs[x]))
        PORTS.append( [PORT + x, devs[x]])
    f.close()

    print("configured ser2net config")

    resetSer2NetService()

    return {"status": "success"}


# Extra Get Commands
@app.get("/ports/by-port-number/{portNum}") # Tested Working
def read_item(portNum: int):
    for x in PORTS:
        if(x[0] == portNum):
            return {"port": x[1]}
    return {"status": "not found"}

#@app.get("/ports/by-usb-path/{usbPath}") # PORTS[] has "/" which screws up the https parsing, needs a bit of refactoring work, idk if I care enough
#def read_item(usbPath: str):
#    for x in PORTS:
#        if(x[1] == usbPath):
#            return {"port": x[0]}
#    return {"status": "not found"}

# Test functions
@app.get("/tests/getSerialConfig/{id}/{path}")
def getPorts(id: int, path: str):
    # Returns list of ports
    return {"return": getSerialConfig(id, path)}

@app.get("/tests/resetSer2NetService")
def testResetSer2NetService():
    # runs resetSer2NetService
    return {"return": resetSer2NetService()}

@app.get("/tests/getSerialDevices")
def testGetSerialDevice():
    # run getSerialDevices
    return {"return": getSerialDevices()}