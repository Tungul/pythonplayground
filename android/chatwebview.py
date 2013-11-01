import android

#  switch library. can I put this in a .py and run import switch?
# not mine
class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration
    
    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args: # changed for v1.5, see below
            self.fall = True
            return True
        else:
            return False

droid = android.Android()
droid.webViewShow('file:///sdcard/sl4a/scripts/text_to_speech.html')
while True:
	map = droid.eventWait()
	print map
	# for case in switch()
	# droid.ttsSpeak(result['data'])