import serial as serialPort
from time import sleep
import threading

import flask

serial = serialPort.Serial('/dev/cu.usbmodem14201')
app = flask.Flask(__name__)

currentport = ''

def readPort():
    global currentport
    while 1:
        inp = str(serial.readline().decode('utf-8')).replace('\n', '')
        currentport = inp
        sleep(0.01)

@app.route('/get', methods=['GET'])
def index():
    print(currentport)
    return currentport

'''
while 1:
    inp = str(serial.readline().decode('utf-8')).replace('\n', '')
    print(inp)
    sleep(0.01)
'''

thread = threading.Thread(target=readPort)
thread.start()
app.run(port=8080)


'''
import requests

while 1:
    print(requests.get('http://127.0.0.1:8080/get').content)
'''
