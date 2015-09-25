__author__ = 'ronnie ashlock'

# A learning script that generates a locator at random locations in the scene. Whee!

from pymel.core import *
import maya.cmds as mc
import maya.mel as mel
import pymel.core as pm
import random
import math

win = window(title="Locator Maker")
##
mc.frameLayout('User_Feedback',label='User Defined Coordinates',width=120,cll=False)
mc.columnLayout()
##
mc.rowLayout(numberOfColumns=2,cw2=(80,10))
mc.text(label='X Coordinate:')
mc.floatField('step_a',precision=2,width=90,value=0.0)
mc.setParent('..')
##
mc.rowLayout(numberOfColumns=2,cw2=(80,10))
mc.text(label='Y Coordinate:')
mc.floatField('step_b',precision=2,width=90,value=0.0)
mc.setParent('..')
##
mc.rowLayout(numberOfColumns=2,cw2=(80,10))
mc.text(label='Z Coordinate:')
mc.floatField('step_c',precision=2,width=90,value=0.0)
mc.setParent('..')
## Button to create locator and center pivot
mc.rowLayout(numberOfColumns=2,cw2=(80,10))
mc.button(label='Make Locator', w=80, c=lambda *args:(spaceLocator(p = [mc.floatField('step_a',q=True,v=True), mc.floatField('step_b',q=True,v=True), mc.floatField('step_c',q=True,v=True)], a = True),CenterPivot()))
showWindow()
