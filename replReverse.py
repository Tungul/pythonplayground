import socket

client = socket.create_connection(("localhost", 8675))

while True:
	line = client.recv(1024)
	print line.replace("\n", "")