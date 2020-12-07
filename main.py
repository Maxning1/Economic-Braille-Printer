#!/usr/bin/env pybricks-micropython

#--------------------
# main.py
# controls the printer
#--------------------


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor
from pybricks.parameters import Port, Stop, Direction, Button
from pybricks.tools import wait, StopWatch, DataLog
from textToBraille import textToBraille
from textwrap import text_wrapping
from textwrap import text_conversion

#Gobal variable
charsPerLine = 14
maxLines = 9


from textReader import fileReader, chooseFile
from textToBraille import textToPoints
from textwrap import text_wrapping


SPEED = 800
PI = 3.1415

ev3 = EV3Brick()
motorX = Motor(Port.C)
motorY = Motor(Port.B)
motorZ = Motor(Port.D)

# HORIZONTAL MOVEMENT 0mm<--------------------->190mm
def moveToX(x):
    assert 0 <= x <= 190, "MOTOR X OUT OF RANGE " + str(x)

    degrees = x * -7.0313
    motorX.run_target(SPEED, degrees, wait=True)
    motorX.hold()

# VERTICAL MOVEMENT 0mm<--------------------->210mm
def moveToY(y):
    assert 0 <= y <= 210, "MOTOR Y OUT OF RANGE " + str(y)

    radius = 16
    degrees = y * (-360/(2*PI*radius))
    motorY.run_target(SPEED, degrees, wait=True)
    motorY.hold()

# PUNCHER MOVEMENT UP 0mm<----------->50mm DOWN
def moveToZ(z):
    assert 0 <= z <= 50, "MOTOR Z OUT OF RANGE " + str(z)
    degrees = z * 7.0313
    motorZ.run_target(SPEED, degrees, wait=True)
    motorZ.hold()

# PUNCHES A HOLE AT X, Y in millimeters
def punch(x, y):
    if x == -1 and y == -1:
        releasePaper()
        loadPaper()
    else:
        moveToX(190-x)
        moveToY(y)
        moveToZ(45)
        moveToZ(35)

# LOADS PAPER
def loadPaper():
    # ask for new paper
    ev3.speaker.say("please load paper")
    done = False
    while not done:
        if len(ev3.buttons.pressed()):
            break
    motorY.run_angle(SPEED, -300, wait=True)
    motorY.hold()
    motorY.reset_angle(0)

def releasePaper():
    moveToY(210)
    motorY.run_angle(SPEED, -300, wait=True)
    motorY.hold()
    motorY.reset_angle(0)

loadPaper()

# IMPORTANT
pointList = textToPoints(text_wrapping(fileReader(chooseFile())))

for x, y in pointList:
    punch(x, y)


releasePaper()
moveToZ(0)
