import android
import sys

droid = android.Android()
for x in sys.version_info:
	droid.makeToast(x)