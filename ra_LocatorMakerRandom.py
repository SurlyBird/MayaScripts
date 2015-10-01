__author__ = 'ronnie ashlock'

# A learning script that generates a locator at random locations in the scene. Whee!

import pymel.core as pmc
import random
import math

pmc.window(title="Random Locator Maker")
pmc.frameLayout('User_Feedback',label='Input',width=200,cll=False)
pmc.columnLayout(bgc=(0.5, 0.0, 0.0))
pmc.rowLayout(numberOfColumns=1, bgc=(0.1, 0.5, 0.25), cal=(1, 'center'))
pmc.button(label='Make a Randomly-Placed Locator',w=200, c=lambda *args:(pmc.spaceLocator(p = [random.uniform(0,12), random.uniform(0,12), random.uniform(0,12)]), pmc.xform(centerPivots=True)))
pmc.setParent('..')

pmc.showWindow()
