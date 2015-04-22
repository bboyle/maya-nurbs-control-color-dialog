# Work in progress - DO NOT USE
# benjamins.boyle@gmail.com
# https://github.com/bboyle/maya-nurbs-control-color-dialog

import maya.cmds as cmds

# get all selected objects
selected = cmds.ls(sl=True)
cmds.setAttr(selected[0] + '.overrideEnabled', True)
# color: 0-31
cmds.setAttr(selected[0] + '.overrideColor', 17) # yellow

# TODO filter list to nurbs?

# nothing selected? exit

# ask for a colour: limited to 0-31 indexed colours
# use the first selected objects color as the default
# colorEditor([hsvValue=[float, float, float]], [mini=boolean], [parent=string], [position=boolean], [result=boolean], [rgbValue=[float, float, float]])

cmds.window()
cmds.frameLayout(labelVisible=False)

# create palette of 32 colours
cmds.palettePort( 'palette', dim=(8, 4))

for i in range(1, 32):
	rgb = cmds.colorIndex(i, q=True)
	cmds.palettePort('palette', edit=True, scc=i)
	cmds.palettePort('palette', edit=True, rgbValue=(i, rgb[0], rgb[1], rgb[2]))

cmds.showWindow()
