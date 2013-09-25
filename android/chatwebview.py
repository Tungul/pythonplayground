import android
import switch

droid = android.Android()
droid.webViewShow('file:///sdcard/sl4a/scripts/text_to_speech.html')
while True:
	map = droid.eventWait()
	print map
	# for case in switch()
	# droid.ttsSpeak(result['data'])