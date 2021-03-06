__author__ = 'ronnie ashlock'

# A learning script that generates a locator at random locations in the scene. Whee!

import pymel.core as pmc
import random
import math

win = pmc.window(title="Locator Maker")
##
pmc.frameLayout('User_Feedback',label='User Defined Coordinates',width=120,cll=False)
pmc.columnLayout()

##

pmc.rowLayout(numberOfColumns=2, bgc=(0.5, 0.0, 0.0), cw2=(80,10))
pmc.text(label='X Coordinate:')
pmc.floatField('step_a',precision=2,width=90,value=0.0)
pmc.setParent('..')

##
pmc.rowLayout(numberOfColumns=2, bgc=(0.0, 0.5, 0.0), cw2=(80,10))
pmc.text(label='Y Coordinate:')
pmc.floatField('step_b',precision=2,width=90,value=0.0)
pmc.setParent('..')

##
pmc.rowLayout(numberOfColumns=2, bgc=(0.0, 0.0, 0.5), cw2=(80,10))
pmc.text(label='Z Coordinate:')
pmc.floatField('step_c',precision=2,width=90,value=0.0)
pmc.setParent('..')

## Button to create locator and center pivot
pmc.rowLayout(numberOfColumns=2,cw2=(80,10))
pmc.button(label='Make Locator', w=80, c=lambda *args:(pmc.spaceLocator(p = [pmc.floatField('step_a',q=True,v=True), pmc.floatField('step_b',q=True,v=True), pmc.floatField('step_c',q=True,v=True)], a = True),pmc.xform(centerPivots=True)))
pmc.showWindow()