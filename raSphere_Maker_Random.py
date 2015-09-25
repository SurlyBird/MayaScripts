__author__ = 'ronnie ashlock'

# A learning script that makes a sphere at random sizes. Whee!

import pymel.core as pmc
import random
import math

win = window(title="Locator Maker")

frameLayout('User_Feedback',label='Input',width=220,cll=True)
pmc.columnLayout()

pmc.rowLayout(numberOfColumns=1,cw1=(80))
pmc.button(label='Make Sphere',w=80, c=lambda *args:polySphere(r = random.uniform(0,12)))
pmc.setParent('..')

showWindow()
