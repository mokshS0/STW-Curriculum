import maestro
import time
import pyttsx3

controller = maestro.Controller(ttyStr='COM7', device=0x0c)
engine = pyttsx3.init()
engine.setProperty('rate', 130)

def voice(audio):
    engine.say(audio)
    engine.runAndWait()

def armSpeed(n):
    for i in [0, 1, 2, 3, 4]:
        controller.setSpeed(i, n)

def fistBump():
    armSpeed(35)
    voice("Fist bump coming up!")
    time.sleep(0.3)
    controller.setTarget(3, 7000)
    controller.setTarget(2, 5000)
    controller.setTarget(1, 3000)
    controller.setTarget(0, 2000)
    time.sleep(2)
    controller.setTarget(3, 4000)
    controller.setTarget(2, 4000)
    time.sleep(3)
    voice("Nice one!")

fistBump()

# CHALLENGE SOLUTION:

# Return arm to neutral standby position
#def standBy():
#   controller.setTarget(0, 6000)
#    controller.setTarget(2, 1000)
#    controller.setTarget(3, 9000)
#    controller.setTarget(4, 10000)
#    time.sleep(2)

#def stretchFistBump():
#    voice("Ready?")
#    time.sleep(0.5)
#    voice("3")
#    time.sleep(1)
#    voice("2")
#    time.sleep(1)
#    voice("1")
#    time.sleep(1)
#    fistBump()
#    voice("Boom!")
#    standBy()

#Loop Solution:
#def stretchFistBump():
#    voice("Ready?")
#    time.sleep(0.5)
#    voice("3")
#    time.sleep(1)
#    voice("2")
#    time.sleep(1)
#    voice("1")
#    time.sleep(1)
#    fistBump()
#    voice("Boom!")
#    standBy()