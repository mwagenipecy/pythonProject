from time import strftime
from datetime import time
import pyttsx3
def CurrentTime():
    engine=pyttsx3.init()
    time_now=strftime('it is '+strftime('%H:%M:%S %p'))
    engine.say(time_now)
    engine.runAndWait()

print(CurrentTime())

