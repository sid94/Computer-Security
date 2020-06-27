import os
import sys
from cryptography.fernet import Fernet


class Key:
    def __init__(self,type):
        self.key = None
        self.keyops(type)
        
    def keyops(self,type):
        try:
            if(not os.path.isfile("key.key") and type == "genpass"):
                self.key = Fernet.generate_key()
                file = open('key.key', 'wb')
                file.write(self.key)
                file.close()
            else:
                file = open('key.key', 'rb')
                self.key = file.read()
                file.close()
        except:
            print("error occured during key read")
            sys.exit()
        
    def getkey(self):
        return self.key