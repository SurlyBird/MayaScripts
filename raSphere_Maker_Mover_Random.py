__author__ = 'ronnie ashlock'

# A learning script that makes a sphere and moves it to a random position. Wee!

from pymel.core import *
import maya.cmds as mc
import maya.mel as mel
import pymel.core as pm
import random
import math

win = window(title="Sphere Randomizer")

frameLayout('User_Feedback',label='Input',width=220,cll=True)
mc.columnLayout()

mc.rowLayout(numberOfColumns=2,cw1=(80))
mc.button(label='Make Sphere',w=80, c=lambda *args:(polySphere(r = random.uniform(0,12)), move(random.uniform(-20.0,20), random.uniform(-20.0,20), random.uniform(-20.0,20)))    )
mc.button(label='Move Sphere',w=80, c=lambda *args:move(random.random(), random.random(), random.random()))
mc.setParent('..')

showWindow()
