import socket
import ssl

#create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


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
#s.close()
securesocket.close()


# full_msg = ''
# while True:
#     msg = s.recv(8)
#     if len(msg) <= 0:
#         break
#     full_msg += msg.decode("utf-8")

# print(full_msg)


# import socket
# import ssl

# # client
# if __name__ == '__main__':

#     HOST = '127.0.0.1'
#     PORT = 1234

#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     sock.setblocking(1);
#     sock.connect((HOST, PORT))

#     context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
#     context.verify_mode = ssl.CERT_REQUIRED
#     context.load_verify_locations('server.pem')
#     context.load_cert_chain(certfile="client.pem", keyfile="client.key")

#     if ssl.HAS_SNI:
#         secure_sock = context.wrap_socket(sock, server_side=False, server_hostname=HOST)
#     else:
#         secure_sock = context.wrap_socket(sock, server_side=False)

#     cert = secure_sock.getpeercert()
#     print(cert)

#     # verify server
#     if not cert or ('commonName', 'test') not in cert['subject'][3]: raise Exception("ERROR")

#     secure_sock.write('hello')
#     print(secure_sock.read(1024))

#     secure_sock.close()
#     sock.close()