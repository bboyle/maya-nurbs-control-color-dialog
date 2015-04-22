import maya.cmds as cmds

# get all selected objects
selectedObjects = cmds.ls(sl=True)

# TODO filter list to nurbs?

# nothing selected? exit

# ask for a colour
# use the first selected objects color as the default

# loop through all selections
	# set the color
