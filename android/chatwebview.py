import android
# import switch
import socket

c = socket.create_connection(("192.168.1.148", 8675))
c.send("connected...\n")

droid = android.Android()
droid.webViewShow('file:///sdcard/sl4a/scripts/chatwebview.html')
while True:
	# data = c.recv(1024)
	# print data.replace("\n", "")
	# droid.eventPost("berp", data)

	map = droid.eventWaitFor("connect").result
	droid.makeToast("got event")
	print map
	# for case in switch()
	# droid.ttsSpeak(result['data'])
