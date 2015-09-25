__author__ = 'ronnie ashlock'

# A learning script that generates a locator at random locations in the scene. Whee!

import pymel.core as pmc
import random
import math

win = window(title="Locator Maker")

frameLayout('User_Feedback',label='Input',width=220,cll=False)
pmc.columnLayout()

pmc.rowLayout(numberOfColumns=1,cw1=(80))
pmc.button(label='Make Locator',w=80, c=lambda *args:(spaceLocator(p = [random.uniform(0,12), random.uniform(0,12), random.uniform(0,12)]), CenterPivot()))
pmc.setParent('..')

showWindow()

