import sys
import os
from cryptography.fernet import Fernet
import base64

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
    sys.exit()

print("please enter User Id")
useridinput = input()
print("please enter password")
passinput = input()

file = open('key.key', 'rb')
key = file.read()

cipher = Fernet(key)


if(useridinput in password):
    decoded = cipher.decrypt(password[useridinput].encode("utf-8"))
    if(str(decoded.decode("utf-8")) == str(passinput)):
        print("password is correct")
    else:
        print("password is incorrect")
else:
    print("User doesnot exist")


sys.exit()    


