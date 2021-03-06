# from config import DEVELOPER_TOKEN, URL
URL = "http://155.248.242.2"
DEVELOPER_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyLCJjb250ZW50IjoiSSBBTSBUSEUgREVWRUxPUEVSIn0.ydKxDB9RGNQKLHcoigvCZCUXQX2PILlZYvdY-f-PaMA"
import requests


def init(unsafe=False):
    if unsafe:
        r = requests.post(
            f"{URL}/dev/init", {'userToken': DEVELOPER_TOKEN, 'unsafe': 'unsafe'})
        # This is because JS cannot understand 'False' as boolean false. It takes it as a string, hence considering it true
    else:
        r = requests.post(f"{URL}/dev/init", {'userToken': DEVELOPER_TOKEN})
    return r.text


def startTrading():
    r = requests.post(f"{URL}/dev/startTrading",
                      {'userToken': DEVELOPER_TOKEN})
    return r.text


def take_a_break():
    r = requests.post(f"{URL}/dev/break", {'userToken': DEVELOPER_TOKEN})
    return r.text


def restart():
    r = requests.post(f"{URL}/dev/restart", {'userToken': DEVELOPER_TOKEN})
    return r.text


def restart_buying_period():
    r = requests.post(f"{URL}/dev/restartBuyingPeriod",
                      {'userToken': DEVELOPER_TOKEN})
    return r.text


def init_memory():
    r = requests.post(f"{URL}/dev/initMemory", {'userToken': DEVELOPER_TOKEN})
    return r.text


def getMemory():
    r = requests.post(f"{URL}/dev/getMemory", {'userToken': DEVELOPER_TOKEN})
    return r.json()


def getDB():
    r = requests.post(f"{URL}/dev/getDB", {'userToken': DEVELOPER_TOKEN})
    return r.json()
