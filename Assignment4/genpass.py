import sys
import os
from cryptography.fernet import Fernet
import base64
from key import Key

class GenPass():
    def __init__(self):
        key = Key("genpass")
        self.key = key.getkey()
        
        self.acceptkey()
        
    def acceptkey(self):
        
        while True:
            print("please enter User Id")
            userid = input()
            print("please enter password")
            password  = input()
            self.writetofile(userid,password)
            print("\nEnter next id and password to be Generated\n")
        
    def writetofile(self,id,password):
        writetype = None
        if(os.path.isfile("password")):
            writetype = "a+"
        else:
            writetype = "w+"
        cipher = Fernet(self.key)
        token = cipher.encrypt(password.encode('utf-8'))   
        with open("password",writetype) as f:
            f.write('{} {}\n'.format(str(id), str(token.decode("utf-8"))))
            f.close()
            
if __name__ == '__main__':
    GenPass()
            

