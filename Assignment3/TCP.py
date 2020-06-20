import socket
import sys

class Socket():
    def __init__(self):
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        except:
            print("Could not create a socket")
            sys.exit()
    
    def getSocket(self):
        return self.s