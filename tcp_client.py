import socket 

target_host = "0.0.0.0"
target_port = 9998

#socket of object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connecting client
client.connect((target_host, target_port))

#sending some data
client.send(b"ABCDEF")

#getting some data
response = client.recv(4096)

print(response.decode())
client.close()