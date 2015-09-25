__author__ = 'ronnie ashlock'

# A learning script that makes a sphere at random sizes. Whee!

import pymel.core as pmc
import random
import math

class SphereMakerMoverRandom():
    def sphere_maker(self):
        pmc.polySphere(r = random.uniform(0,12))
        pmc.setParent('..')
    def sphere_mover(self):
        pmc.move([random.random(), random.random(), random.random()])
        pmc.setParent('..')
        
     
    pmc.window(width=200, title="Sphere Randomizer")
    pmc.columnLayout(adjustableColumn = True, bgc=(0.5, 0.0, 0.5))
    pmc.rowLayout(numberOfColumns=2, bgc=(0.25, 0.75, 0.1), cw2=(100,100), cal=(2,'left'))
    pmc.button(label="Make Sphere", command=sphere_maker)
    pmc.button(label="Move Sphere", command=sphere_mover)
    
    
    pmc.showWindow()