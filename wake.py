import time
from datetime import datetime

# Check if pyautogui is installed, if not, install it
try:
    import pyautogui
except ImportError:
    print("pyautogui is not installed. Installing now...")
    import subprocess
    subprocess.check_call(["pip", "install", "pyautogui"])
    import pyautogui

currentDateAndTime = datetime.now()
hour = currentDateAndTime.hour
endHour = 17

while hour < endHour:
	time.sleep(5)
	pyautogui.moveTo(900,700)
	time.sleep(5)
	pyautogui.moveTo(1000,500)
	currentDateAndTime = datetime.now()
	hour = currentDateAndTime.hour	
