import os
import sys


class ReadFile():
    def __init__(self):
        self.password = {}
        self.readPasswordFile()
        
    def readPasswordFile(self):
        # msg = None
        # try:
            if(os.path.isfile('password')):
                with open("password", "r") as file:
                    for line in file:
                        dummy = line.split()
                        if(dummy[0] not in self.password):
                            self.password[dummy[0]] = dummy[1]
                file.close()
            else:
                print("password file does not exists")
                sys.exit()
        # except msg:
        #     print("Error occured during password creation")
            
    def getPasswordData(self):
        return self.password