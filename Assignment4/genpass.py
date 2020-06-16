import sys
import os
from cryptography.fernet import Fernet
import base64


print("please enter User Id")
userid = input()
print("please enter password")
password  = input()

writetype = None
if(os.path.isfile("password")):
    writetype = "a+"
else:
    writetype = "w+"
    

key = None

if(not os.path.isfile("key.key")):
    key = Fernet.generate_key()
    file = open('key.key', 'wb')
    file.write(key)
    file.close()
else:
    file = open('key.key', 'rb')
    key = file.read()

cipher = Fernet(key)

token = cipher.encrypt(password.encode('utf-8'))
    
with open("password",writetype) as f:
    f.write('{} {}\n'.format(str(userid), str(token.decode("utf-8"))))
    f.close()
    
sys.exit() 