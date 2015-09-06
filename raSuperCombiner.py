__author__ = 'ronnie ashlock'

# Consolidates a lot of reused workflow procedures in one handy GUI.

import pymel.core as pmc
import maya.mel as mel

class SuperCombiner():

    def combine_all(self):
        pmc.select(all = True)
        pmc.polyUnite()

    def combine_selected(self):
        pmc.polyUnite()

    def separate_all(self):
        pmc.select(all = True)
        pmc.polySeparate()

    def separate_selected(self):
        pmc.polySeparate()

    def nuke_history(self):
        pmc.general.delete(constructionHistory=True)

    def reset_transform(self):
        pmc.makeIdentity(t = True, a = False)

    def freeze_transform(self):
        pmc.makeIdentity(t = True, a = True)
        
    def fix_pivot(self):
        pmc.xform(centerPivots = True)
        
    def set_to_origin(self):
        mel.eval('numericalInputChangeCommand abs')
        pmc.makeIdentity(t = True, a = True)

    pmc.window(width = 200, title ='Super Combiner')
    pmc.columnLayout(adjustableColumn = True)
    pmc.button(label = "Combine Selected", command = combine_selected)
    pmc.button(label = "Separate Selected", command = separate_selected)
    pmc.button(label = "Combine All", command = combine_all)
    pmc.button(label = "Separate All", command = separate_all)
    pmc.button(label = "Reset Transforms", command = reset_transform)
    pmc.button(label = "Freeze Transforms", command = freeze_transform)
    pmc.button(label = "Delete History", command = nuke_history)
    pmc.button(label = "Center Pivot", command = fix_pivot)
    pmc.button(label = "Move to Origin", command=set_to_origin)

    pmc.showWindow()

SuperCombiner()