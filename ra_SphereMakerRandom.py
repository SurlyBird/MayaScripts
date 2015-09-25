__author__ = 'ronnie ashlock'

# A learning script that makes a sphere at random sizes. Whee!

import pymel.core as pmc
import random
import math

class SphereMakerRandom():
    def sphere_maker(self):
        pmc.polySphere(r = random.uniform(0,12))
        pmc.setParent('..')
        
     
    pmc.window(width=200, title="Sphere Maker")
    pmc.columnLayout(adjustableColumn = True)
    
    pmc.button(label="Make Sphere", command=sphere_maker)
    
    
    pmc.showWindow()
