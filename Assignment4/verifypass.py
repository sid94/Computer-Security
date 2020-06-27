import sys
import os
from cryptography.fernet import Fernet
import base64
from key import Key

class VerifyPass:
    def __init__(self):
        key = Key("verifypass")
        self.key = key.getkey()
        self.password = self.getpassworddata()
        
    def getpassworddata(self):
        password = {}
        if(os.path.isfile("password")):
            with open("password", "r") as file:
                for line in file:
                    dummy = line.split()
                    if(dummy[0] not in password):
                        password[dummy[0]] = str(dummy[1])  
                file.close()
        else:
            print("password file doesnt exist!!")
            sys.exit(0)
        return password
    
    def verifypass(self):
        print("please enter User Id")
        useridinput = input()
        print("please enter password")
        passinput = input()
        
        cipher = Fernet(self.key)

        if(useridinput in self.password):
            decoded = cipher.decrypt(self.password[useridinput].encode("utf-8"))
            if(str(decoded.decode("utf-8")) == str(passinput)):
                print("password is correct")
            else:
                print("password is incorrect")
        else:
            print("ID does not exist.")
        
        sys.exit()
        
if __name__ == '__main__':
    v = VerifyPass()
    v.verifypass()


