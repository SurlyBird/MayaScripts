from pymel.core import *
import maya.cmds as mc
import maya.mel as mel
import pymel.core as pm
import random
import math



win = window(title="Locator Maker")

frameLayout('User_Feedback',label='Input',width=220,cll=False)
mc.columnLayout()

mc.rowLayout(numberOfColumns=1,cw1=(80))
mc.button(label='Make Locator',w=80, c=lambda *args:(spaceLocator(p = [random.uniform(0,12), random.uniform(0,12), random.uniform(0,12)]), CenterPivot()))
mc.setParent('..')

showWindow()

