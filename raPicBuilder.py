__author__ = 'ronnie ashlock'

# This is script is designed to load a pre-defined shape library
# and build a Picatinny rail system.


import pymel.core as pmc

def pic_tin():
    for i in range(0, 10):
        x = 0
        x = x+i


        #pmc.polyCube(n='Dude', w=0.5)

        #Switch from object to edge mode and select top edges
        #pmc.selectMode(co=True)
        #pmc.selectType(eg=True)
        #pmc.select(all=True)

        #pmc.polyBevel(fraction=0.25)
        #pmc.selectMode(co=False)
        pmc.duplicate()
        pmc.move(0, 0, x)

    pmc.select(all=True)
    pmc.polyUnite()
    pmc.delete(ch=True)

    pmc.rename()

pic_tin()
