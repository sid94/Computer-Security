import socket
import ssl
import os
import sys
from TCP import Socket
from readfile import ReadFile

class Server:
    def __init__(self,param):
        tcp =  Socket()
        readfile = ReadFile()
        self.s = tcp.getSocket()
        self.password = {} 
        self.password = readfile.getPasswordData()
        self.s.bind((socket.gethostname(), 1234))
        self.s.listen(5)
        
        self.securesocket()
        
    def securesocket(self):
        #while True:
        # now our endpoint knows about the OTHER endpoint.
            clientsocket, address = self.s.accept()
            securesocket = ssl.wrap_socket(clientsocket, server_side=True,certfile="cert/skolhap1.pem", keyfile="cert/privkey.pem", ssl_version=ssl.PROTOCOL_TLSv1_2)
            
            print(f"Connection from {address} has been established.")
            
            userid = securesocket.recv(1024)
            rawpassword = securesocket.recv(1024)
            
            print(f"Userid : {userid} and Password : {rawpassword} received")
            
            if(userid and rawpassword):
                if(userid.decode('utf-8') in self.password and self.password[str(userid.decode('utf-8'))] == str(rawpassword.decode('utf-8'))):
                    securesocket.send(bytes("correct ID and password","utf-8"))
                else:
                    securesocket.send(bytes("incorrect ID and password","utf-8"))
    
            securesocket.close()
        

if __name__ == '__main__':
    Server(sys.argv[1:])
    
    

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind((socket.gethostname(), 1234))
# s.listen(5)


# password = {}
# def readpasswordFile():
#     if(os.path.isfile('password')):
#         with open("password", "r") as file:
#             for line in file:
#                 dummy = line.split()
#                 if(dummy[0] not in password):
#                     password[dummy[0]] = dummy[1]
#             file.close()
#     else:
#         print("password file does not exists")
#         sys.exit()
        
# readpasswordFile()

# while True:
#     # now our endpoint knows about the OTHER endpoint.
#     clientsocket, address = s.accept()
#     securesocket = ssl.wrap_socket(clientsocket, server_side=True,certfile="cert/skolhap1.pem", keyfile="cert/privkey.pem", ssl_version=ssl.PROTOCOL_TLSv1_2)
        
#     userid = securesocket.recv(1024)
#     rawpassword = securesocket.recv(1024)
    
#     print(f"Connection from {address} has been established.")
#     #clientsocket.send(bytes("Hey there!!!","utf-8"))
#     print(f"userid :- {userid.decode('utf-8')} , password :- {rawpassword.decode('utf-8')}")

#     if(userid and rawpassword):
#         print(str(password[userid.decode('utf-8')]))
#         print(str(rawpassword.decode('utf-8')))
#         if(userid.decode('utf-8') in password and password[str(userid.decode('utf-8'))] == str(rawpassword.decode('utf-8'))):
#             securesocket.send(bytes("correct ID and password","utf-8"))
#         else:
#             securesocket.send(bytes("incorrect ID and password","utf-8"))
               
    
#     securesocket.close()
