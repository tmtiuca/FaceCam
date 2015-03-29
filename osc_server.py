from liblo import *
import sys
import time
import subprocess as sp
import webbrowser
from math import*

average_short = 0
average_long = 0
counter_long = 0
counter_short = 0

moving_average_short = [] 
moving_average_long = [] 

def vibration_short (moving_average_short):
    global average_short
    average_short = 0
    if len(moving_average_short) == 0:
        return 0
    for i in moving_average_short:
        average_short += i
    average_short = average_short / len(moving_average_short)
    if abs(average_short) < 0.2:
        return True
    return False

def vibration_long (moving_average_long):
    global average_long 
    average_long = 0
    if len(moving_average_long) == 0:
        return 0
    for i in moving_average_long:
        print 'hello'
        print i
        average_long += i
    average_long = average_long / len(moving_average_long)
    if abs(average_long) < 0.1:
        return True
    return False

class MuseServer(ServerThread):

    #listen for messages on port 5001
    def __init__(self):
        ServerThread.__init__(self, 5001)

    @make_method('/muse/elements/experimental/mellow', 'f')
    def con_callback(self, path, args):
        global counter_long
        global counter_short 

        print '___________________________________________________________________________________________________'
        print args 
        # replace counter based on the effect of time.sleep function below
        counter_long = counter_long + 1 
        counter_short = counter_short + 1
        args = float(args[0])
        moving_average_short.append(args)
        moving_average_short[1:5] # splice frorm 1-1000
        if (vibration_short(moving_average_short)) == True:
            url = 'http://www.google.com'
            c = webbrowser.get('safari')
            c.open(url)
        if counter_long == 3:
            moving_average_long.append(args)
            moving_average_long[1:10]
            counter_long == 0
            if (vibration_long(moving_average_long)) == True:
                #xfoil = sp.Popen(['/Applications/Firefox.app/Contents/MacOS/Firefox'], stdin=sp.PIPE, stdout=sp.PIPE)
                controller = webbrowser.get('Firefox')
                controller.open('http://www.google.com')
try:
    server = MuseServer()
except ServerError, err:
    print str(err)
    sys.exit()

server.start()

if __name__ == "__main__":
    while 1:
        time.sleep(1)
