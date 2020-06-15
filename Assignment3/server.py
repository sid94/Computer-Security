import socket
import ssl
import os
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)


password = {}
def readpasswordFile():
    if(os.path.isfile('password')):
        with open("password", "r") as file:
            for line in file:
                dummy = line.split()
                if(dummy[0] not in password):
                    password[dummy[0]] = dummy[1]
    else:
        print("password file does not exists")
        sys.exit()
        
readpasswordFile()

while True:
    # now our endpoint knows about the OTHER endpoint.
    clientsocket, address = s.accept()
    securesocket = ssl.wrap_socket(clientsocket, server_side=True,certfile="cert/skolhap1.pem", keyfile="cert/privkey.pem", ssl_version=ssl.PROTOCOL_TLSv1_2)
        
    userid = securesocket.recv(1024)
    rawpassword = securesocket.recv(1024)
    
    print(f"Connection from {address} has been established.")
    #clientsocket.send(bytes("Hey there!!!","utf-8"))
    print(f"userid :- {userid.decode('utf-8')} , password :- {rawpassword.decode('utf-8')}")

    if(userid and rawpassword):
        print(str(password[userid.decode('utf-8')]))
        print(str(rawpassword.decode('utf-8')))
        if(userid.decode('utf-8') in password and password[str(userid.decode('utf-8'))] == str(rawpassword.decode('utf-8'))):
            securesocket.send(bytes("correct ID and password","utf-8"))
        else:
            securesocket.send(bytes("incorrect ID and password","utf-8"))
               
    
    securesocket.close()
    #s.close()
        
        

# #!/bin/usr/env python
# import socket
# import ssl
# import pprint

# #server
# if __name__ == '__main__':

#     HOST = '127.0.0.1'
#     PORT = 1234

#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#     server_socket.bind((HOST, PORT))
#     server_socket.listen(10)

#     client, fromaddr = server_socket.accept()
#     secure_sock = ssl.wrap_socket(client, server_side=True, ca_certs = "client.pem", certfile="server.pem", keyfile="cert/privkey.pem", cert_reqs=ssl.CERT_REQUIRED,
#                            ssl_version=ssl.PROTOCOL_TLSv1_2)

#     print(repr(secure_sock.getpeername()))
#     print(secure_sock.cipher())
#     print(pprint.pformat(secure_sock.getpeercert()))
#     cert = secure_sock.getpeercert()
#     print(cert)

#     # verify client
#     if not cert or ('commonName', 'test') not in cert['subject'][3]: raise Exception("ERROR")

#     try:
#         data = secure_sock.read(1024)
#         secure_sock.write(data)
#     finally:
#         secure_sock.close()
#         server_socket.close()