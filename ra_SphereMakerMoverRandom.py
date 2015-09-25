__author__ = 'ronnie ashlock'

# A learning script that makes a sphere and moves it to a random position. Whee!

import pymel.core as pmc
import random
import math

win = window(title="Sphere Randomizer")

frameLayout('User_Feedback',label='Input',width=220,cll=True)
pmc.columnLayout()

pmc.rowLayout(numberOfColumns=2,cw1=(80))
pmc.button(label='Make Sphere',w=80, c=lambda *args:(polySphere(r = random.uniform(0,12)), move(random.uniform(-20.0,20), random.uniform(-20.0,20), random.uniform(-20.0,20)))    )
pmc.button(label='Move Sphere',w=80, c=lambda *args:move(random.random(), random.random(), random.random()))
pmc.setParent('..')

showWindow()
