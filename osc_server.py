from liblo import *
import sys
import time

import lua
lg = lua.globals()

lua.execute("onForegroundWindowChange")
lua.execute("onPeriodic")
lua.execute("onPoseEdge")

class MuseServer(ServerThread):

    moving_average_short = []
    moving_average_long = []
    counter_short = 0       # every 300
    counter_long = 0        # every 600


    #listen for messages on port 5001
    def __init__(self):
        ServerThread.__init__(self, 5001)

    @make_method('/muse/elements/experimental/mellow', 'f')
    def con_callback(self, path, args):
        print '___________________________________________________________________________________________________'
        print args 
        # replace counter based on the effect of time.sleep function below
        counter_long ++
        counter_short ++
        moving_average_short.append()
        moving_average_short.slice[1:300] # splice frorm 1-1000
        counter_short = 0
        if (vibration_short(moving_average_short)):
                lua.execute("Vibrate")
        if counter_long == 3:
            moving_average_long.append()
            moving_average_long.slice[1:600]
            counter_long == 0
            if (vibration_long(moving_average_long)):
                lua.execute("")

try:
    server = MuseServer()
except ServerError, err:
    print str(err)
    sys.exit()

server.start()

if __name__ == "__main__":
    while 1:
        time.sleep(10)
