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

moving_average_short = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
moving_average_long = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 

class MuseServer(ServerThread):

    #listen for messages on port 5001
    def __init__(self):
        ServerThread.__init__(self, 5001)

    @make_method('/muse/elements/experimental/mellow', 'f')
    def con_callback(self, path, args):
        tempShortAvg = moving_average_short[1:29]
        tempLongAvg = moving_average_long[1:599]
        print '___________________________________________________________________________________________________'
        print args 
        # replace counter based on the effect of time.sleep function below
        counter_long += 1 
        counter_short += 1
        args = float(args[0])
        tempShortAvg.append(args)
        tempLongAvg.append(args)
        
        average_short = sum(tempShortAvg)/30
        average_long = sum(tempLongAvg)/600

        moving_average_short = tempShortAvg
        moving_average_long = tempLongAvg

        if average_short < 0.1:
            url = 'http://www.google.com'
            c = webbrowser.get('safari')
            c.open(url)
        if average_long < 0.25:
            url = 'http://www.google.com'
            c = webbrowser.get('safari')
            c.open(url)
try:
    server = MuseServer()
except ServerError, err:
    print str(err)
    sys.exit()

server.start()

if __name__ == "__main__":
    while 1:
        time.sleep(1)
