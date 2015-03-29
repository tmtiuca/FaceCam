from liblo import *
import sys
import time

class MuseServer(ServerThread):
    #listen for messages on port 5001
    def __init__(self):
        ServerThread.__init__(self, 5001)

    @make_method('/muse/elements/experimental/mellow', 'f')
    def con_callback(self, path, args):
        print '___________________________________________________________________________________________________'
        print "mellow: "
        print args

try:
    server = MuseServer()
except ServerError, err:
    print str(err)
    sys.exit()

server.start()

if __name__ == "__main__":
    while 1:
        time.sleep(1)
