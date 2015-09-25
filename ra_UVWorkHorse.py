__author__ = 'ronnie ashlock'

# A set of commonly-used UV tasks bundled into a little GUI.

import pymel.core as pmc

class UVMover():
    def uv_editor(self):
        pmc.runtime.TextureViewWindow()
    def uv_selector(self):
        pmc.select('.f[0:*]')
    def uv_unselector(self):
        pmc.select(cl=True)
    def move_up(self):
        pmc.polyEditUV(u=0.0, v=1.0)
    def move_down(self):
        pmc.polyEditUV(u=0.0, v=-1.0)
    def move_left(self):
        pmc.polyEditUV(u=-1.0, v=0.0)
    def move_right(self):
        pmc.polyEditUV(u=1.0, v=0.0)
        
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


    pmc.window(width=200, title='UV WorkHorse')
    pmc.columnLayout(adjustableColumn = True)
    
    pmc.button(label = "Launch UV Editor", command = uv_editor)
    pmc.button(label = "Combine Selected", command = combine_selected)
    pmc.button(label = "Separate Selected", command = separate_selected)
    pmc.button(label = "Combine All", command = combine_all)
    pmc.button(label = "Separate All", command = separate_all)
    pmc.button(label = "Select UV Shell", command = uv_selector)
    pmc.button(label = "Deselect UV Shell", command = uv_unselector)
    pmc.button(label = "Move Shell Up 1.0", command = move_up)
    pmc.button(label = "Move Shell Down 1.0", command = move_down)
    pmc.button(label = "Move Shell Left 1.0", command = move_left)
    pmc.button(label = "Move Shell Right 1.0", command = move_right)


    pmc.showWindow()