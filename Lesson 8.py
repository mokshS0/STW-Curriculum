import maestro
import time

# Initialize the Maestro servo controller
controller = maestro.Controller(ttyStr='COM7', device=0x0c)  # Adjust COM port as needed
controller.setTarget(17, 3000)  # Power on

# Set speed for arm movement
def armSpeed(n):
    controller.setSpeed(0, n)
    controller.setSpeed(1, n)
    controller.setSpeed(2, n)
    controller.setSpeed(3, n)
    controller.setSpeed(4, n)
    controller.setSpeed(6, n)
    controller.setSpeed(7, n)
    controller.setSpeed(8, n)
    controller.setSpeed(9, n)
    controller.setSpeed(10, n)

# Set robot to default neutral arm pose
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

# Perform handshake using a while loop
def handshake():
    armSpeed(35)
    time.sleep(3)
    controller.setTarget(3, 6000)  # Move shoulder
    controller.setTarget(2, 5000)  # Raise elbow
    controller.setTarget(1, 3000)  # Turn elbow
    time.sleep(1)

    i = 0
    while i < 2:
        controller.setTarget(2, 6000)  # Shake up
        time.sleep(0.75)
        controller.setTarget(2, 4000)  # Shake down
        time.sleep(0.75)
        i += 1

    time.sleep(1)
    standBy()

# Run it
handshake()
