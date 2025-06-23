import maestro
import time
import pyttsx3
import sys

# Initialize the Maestro servo controller
controller = maestro.Controller(ttyStr='COM7', device=0x0c)  # Adjust port if needed
engine = pyttsx3.init()
engine.setProperty('rate', 130)  # Adjust speaking speed

# Voice function
def voice(text):
    engine.say(text)
    engine.runAndWait()

# Set servo speed for smoother motion
def armSpeed(n):
    for i in [0, 1, 2, 3, 4, 6, 7, 8, 9, 10]:
        controller.setSpeed(i, n)

# Set arm to a safe resting position
def standBy():
    controller.setTarget(0, 6000)
    controller.setTarget(1, 4000)
    controller.setTarget(2, 1000)
    controller.setTarget(3, 9000)
    controller.setTarget(4, 10000)
    controller.setTarget(6, 3000)
    controller.setTarget(7, 10000)
    controller.setTarget(8, 9000)
    controller.setTarget(9, 2000)
    controller.setTarget(10, 1000)
    controller.setTarget(12, 6000)
    controller.setTarget(13, 6000)
    time.sleep(3)

# Power functions
def on():
    controller.setTarget(17, 3000)

def off():
    controller.setTarget(17, 7000)

# Grabbing function
def bottleGrab():
    armSpeed(35)
    controller.setTarget(8, 2000)   # Move arm down
    controller.setTarget(9, 4000)
    time.sleep(1)
    
    voice("I will hold your bottle in a sec")
    time.sleep(0.5)
    voice("Holding now")
    controller.setTarget(6, 8000)   # Close grip
    time.sleep(8)
    
    voice("Here is your bottle back")
    voice("Letting go in 3 seconds")
    time.sleep(3)
    controller.setTarget(6, 6000)   # Open grip
    time.sleep(1)
    standBy()

# Run the program
on()
print("Power on")
time.sleep(2)

bottleGrab()

off()
print("Power off")
controller.close()
sys.exit()
