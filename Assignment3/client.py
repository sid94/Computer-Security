import socket
import ssl
from TCP import Socket
import sys

#create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


class Client:
    def __init__(self,param):
        tcp =  Socket()
        self.s = tcp.getSocket()
        
        self.securesocket()
        
    
    def securesocket(self):
        # create and a secure socket using certifcate and connect 
        securesocket = ssl.wrap_socket(s,ca_certs="cert/skolhap1.pem",cert_reqs=ssl.CERT_REQUIRED)
        securesocket.connect((socket.gethostname(), 1234))

        print("Enter User Id")
        userid = input()
        print("Enter User Password")
        password = input()

        #send message
        securesocket.send(bytes(userid,"utf-8"))
        securesocket.send(bytes(password,"utf-8"))

        #receive response and print
        reply = securesocket.recv(1024)
        print(reply.decode("utf-8"))

        #close connection
        securesocket.close()

if __name__ == '__main__':
    Client(sys.argv[1:])