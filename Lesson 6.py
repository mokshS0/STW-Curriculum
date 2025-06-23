import maestro
import time
import random
import pyttsx3

# Setup
engine = pyttsx3.init()
engine.setProperty('rate', 130)
controller = maestro.Controller(ttyStr='COM7', device=0x0c)

# Voice function
def voice(text):
    engine.say(text)
    engine.runAndWait()

# Movement setup
def armSpeed(n):
    for ch in [0, 1, 2, 3, 4, 6, 7, 8, 9, 10]:
        controller.setSpeed(ch, n)

def standBy():
    controller.setTarget(0, 1000)
    controller.setTarget(1, 1000)
    controller.setTarget(2, 10000)
    controller.setTarget(3, 1000)
    controller.setTarget(4, 10000)
    controller.setTarget(6, 1000)
    controller.setTarget(7, 10000)
    controller.setTarget(8, 1000)
    controller.setTarget(9, 10000)
    controller.setTarget(10, 1000)
    controller.setTarget(12, 6000)
    controller.setTarget(13, 6000)
    time.sleep(1)

# Gesture preparation and actions
def RPSInit():
    controller.setTarget(6, 10000)
    controller.setTarget(8, 9000)
    time.sleep(0.3)
    controller.setTarget(8, 2000)
    time.sleep(0.3)

def Rock():
    controller.setTarget(7, 2000)
    controller.setTarget(6, 10000)
    time.sleep(0.4)

def Paper():
    controller.setTarget(7, 1000)
    controller.setTarget(6, 1000)
    time.sleep(0.4)

def Sciccors():
    controller.setTarget(6, 1000)
    time.sleep(0.4)

# Full game
def playRPS():
    standBy()
    armSpeed(20)

    voice("Let's play Rock, Paper, Scissors!")
    voicecallRPS = ["Rock", "Paper", "Scissors", "Shoot"]
    
    for word in voicecallRPS:
        RPSInit()
        voice(word)
        time.sleep(0.5)

    move = random.choice([1, 2, 3])

    if move == 1:
        Sciccors()
        voice("Scissors!")
    elif move == 2:
        Paper()
        voice("Paper!")
    else:
        Rock()
        voice("Rock!")

    time.sleep(1)
    standBy()

# Run the game
playRPS()
