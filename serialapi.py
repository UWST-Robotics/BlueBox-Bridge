from fastapi import FastAPI

app = FastAPI()

IP = "192.168.0.1"
PORT = 8111

YAMLHEADER = """
%YAML 1.1
---


"""

ports = []

def getSerialConfig(id: int, path: str):
    return f"""
    connection: &serialcon{id}
    accepter: telnet,tcp, {IP}, {PORT + id}
    enable: on
    options:
        kickolduser: true
    connector: serialdev, {path}, local
    """

#get path of serial devices and assign ids

@app.get("/")
def ping():
    return {"ping": "pong"}

@app.get("/ports") # Returns list of ports
def getPorts():
    return {"ports": f"{ports}"}

@app.get("/ports") # Returns list of ports
def setPorts():
    # getSerialDevices
    # 
    return {"ports": f"{ports}"}



# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}




#assign ports for each serial device




