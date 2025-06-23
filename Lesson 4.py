import time
import maestro  # Correct library

# Initialize the Maestro controller
controller = maestro.Controller(ttyStr='COM7')  # Adjust COM port as needed

def armSpeed(n):
    controller.setSpeed(0, n)
    controller.setSpeed(1, n)
    controller.setSpeed(2, n)
    controller.setSpeed(3, n)
    controller.setSpeed(4, n)

def wave():
    armSpeed(35)
    controller.setTarget(0, 10000)
    controller.setTarget(1, 10000)
    controller.setTarget(2, 8000)
    controller.setTarget(3, 5000)
    time.sleep(1)
    controller.setTarget(4, 7000)
    time.sleep(0.75)
    controller.setTarget(4, 10000)
    time.sleep(0.75)
    controller.setTarget(4, 7000)
    time.sleep(0.75)
    controller.setTarget(4, 10000)

# Run it
wave()
