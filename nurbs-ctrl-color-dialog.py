import maya.cmds as cmds

# get all selected objects
# selected = cmds.ls(sl=True)

# TODO filter list to nurbs?

# nothing selected? exit

# ask for a colour
# use the first selected objects color as the default
# colorEditor([hsvValue=[float, float, float]], [mini=boolean], [parent=string], [position=boolean], [result=boolean], [rgbValue=[float, float, float]])

result = cmds.colorEditor()
buffer = result.split()
# if a color was chosen
if '1' == buffer[3]:
	values = cmds.colorEditor(query=True, rgb=True)
	print 'RGB = ' + str(values)
	alpha = cmds.colorEditor(query=True, alpha=True)
	print 'Alpha = ' + str(alpha)

	# loop through all selections
	# for o in selected:
		# set the color
		# print o.name

else:
	print 'Editor was dismissed'


