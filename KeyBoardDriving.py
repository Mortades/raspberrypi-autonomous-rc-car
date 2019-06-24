# CamJam EduKit 3 - Robotics
# Worksheet 4 - Driving and Turning
# A = Right Motor
# B = Left Motor
import RPi.GPIO as GPIO  # Import the GPIO Library
import time  # Import the Time library
import getch

# Set the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set variables for the GPIO motor pins
pinMotorAForwards = 10
pinMotorABackwards = 9
pinMotorBForwards = 8
pinMotorBBackwards = 7

# Set the GPIO Pin mode
GPIO.setup(pinMotorAForwards, GPIO.OUT)
GPIO.setup(pinMotorABackwards, GPIO.OUT)
GPIO.setup(pinMotorBForwards, GPIO.OUT)
GPIO.setup(pinMotorBBackwards, GPIO.OUT)


# Turn all motors off
def stopmotors():
    GPIO.output(pinMotorAForwards, 0)
    GPIO.output(pinMotorABackwards, 0)
    GPIO.output(pinMotorBForwards, 0)
    GPIO.output(pinMotorBBackwards, 0)


# Turn both motors forwards
def forwards():
    GPIO.output(pinMotorAForwards, 1)
    GPIO.output(pinMotorABackwards, 0)
    GPIO.output(pinMotorBForwards, 1)
    GPIO.output(pinMotorBBackwards, 0)


# Turn both motors backwards
def backwards():
    GPIO.output(pinMotorAForwards, 0)
    GPIO.output(pinMotorABackwards, 1)
    GPIO.output(pinMotorBForwards, 0)
    GPIO.output(pinMotorBBackwards, 1)


# Turn left
def left():
    GPIO.output(pinMotorAForwards, 0)
    GPIO.output(pinMotorABackwards, 1)
    GPIO.output(pinMotorBForwards, 1)
    GPIO.output(pinMotorBBackwards, 0)
# Homebrew WideTurnRight
def WideRightTurn(duration = 1):
    GPIO.output(pinMotorABackwards, 0)
    GPIO.output(pinMotorBBackwards, 0)
    GPIO.output(pinMotorBForwards, 1)
# Loop for 1 second per each duration turning A on and off to replicate half speed
    for i in range(duration):
         GPIO.output(pinMotorAForwards, 1)
         time.sleep(0.5)
         GPIO.output(pinMotorAForwards, 0)
         time.sleep(0.5)

# Homebrew WideTurnLeft
def WideLeftTurn(duration = 1):
    GPIO.output(pinMotorBBackwards, 0)
    GPIO.output(pinMotorABackwards, 0)
    GPIO.output(pinMotorAForwards, 1)
# Loop for 1 second per each duration turning A on and off to replicate half speed
    for i in range(duration):
         GPIO.output(pinMotorBForwards, 1)
         time.sleep(0.5)
         GPIO.output(pinMotorBForwards, 0)
         time.sleep(0.5)
         
# Turn Right
def right():
    GPIO.output(pinMotorAForwards, 1)
    GPIO.output(pinMotorABackwards, 0)
    GPIO.output(pinMotorBForwards, 0)
    GPIO.output(pinMotorBBackwards, 1)

# WideRightTurn(5)
# WideLeftTurn(5)
# forwards()
# time.sleep(1)  # Pause for 1 second
#
# #left()
# #time.sleep(0.5)  # Pause for half a second
#
# backwards()
# time.sleep(1)
#
# #right()
# #time.sleep(0.5)
#
# #backwards()
# #time.sleep(0.5)
#
# stopmotors()

while True:
    keyboard_input = getch.getche()
    if keyboard_input == 'w':
        forwards()
    if keyboard_input == 's':
        backwards()
    if keyboard_input == " ":
        stopmotors()
    if keyboard_input == "a":
        left()
    if keyboard_input == "d":
        right()

GPIO.cleanup()
