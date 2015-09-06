__author__ = 'ronnie ashlock'

# A learning script that makes a sphere at random sizes. Whee!

from pymel.core import *
import maya.cmds as mc
import maya.mel as mel
import pymel.core as pm
import random
import math

win = window(title="Locator Maker")

frameLayout('User_Feedback',label='Input',width=220,cll=True)
mc.columnLayout()

mc.rowLayout(numberOfColumns=1,cw1=(80))
mc.button(label='Make Sphere',w=80, c=lambda *args:polySphere(r = random.uniform(0,12)))
mc.setParent('..')

showWindow()
