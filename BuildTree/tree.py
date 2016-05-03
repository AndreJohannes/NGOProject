import xml.etree.ElementTree as ET
from PIL import Image
import aggdraw
import math
import random 

class Node:

	def __init__(self, parent, absolut_position, girth, leave):
		self.parent = parent
		self.children = []
		self.girth = girth
		self.has_leave = leave
		self.leave_size = 20
		self.leave_color = (random.randint(40,180), random.randint(120,250), random.randint(0,50))
		self._absolut_position = absolut_position
		if parent is None:
			self.position = absolut_position
		else:
			self.position = [absolut_position[0]-parent._absolut_position[0],
				absolut_position[1]-parent._absolut_position[1]]

	def addChild(self, absolut_position, girth, leave):
		node = Node(self, absolut_position, girth, leave)
		self.children.append(node)
		return node

	def shrink(self, parent):
		if parent is not None:
			x = self.position[0]
			y = self.position[1]
			length = math.sqrt( x*x + y*y )
			if length > 0:
				factor = max(( length - 0.5 ) / length ,0)
			else:
				factor = 0
			self.position[0] = factor * x
			self.position[1] = factor * y
			self.girth = max(1, self.girth*0.975)
			self.leave_size = max(4, self.leave_size*0.975)
			self._absolut_position = [parent._absolut_position[0] + self.position[0],
				parent._absolut_position[1] + self.position[1]]
		for child in self.children:
			child.shrink(self)


def addChildrenFromXML(parent, node):
	for element in parent.getchildren():
		girth = 1
		leave = False
		if(element.attrib.has_key("girth")):
			girth = float(element.attrib["girth"])
		if(element.attrib.has_key("leave")):
			leave = True	
		_node = node.addChild([int(element.attrib["pos_x"]),
			int(element.attrib["pos_y"])],girth, leave)
		addChildrenFromXML(element, _node) 


678,501
root = ET.parse("tree.xml").getroot()
node = Node(None, [329,428],1, False)
addChildrenFromXML(root, node)

def paint_branches(parent, offset, im):
	for node in parent.children:
		d = aggdraw.Draw(im)
		p = aggdraw.Pen("black", node.girth)
		d.line((parent._absolut_position[0]+349,parent._absolut_position[1]+73
			,node._absolut_position[0]+349,node._absolut_position[1]+73),p)
		d.flush()
		paint_branches(node, [offset[0]+node.position[0],
			offset[1]+node.position[1]], im)

def paint_leaves(parent, offset, im):
	for node in parent.children:
		if node.has_leave:
			d = aggdraw.Draw(im)
			p = aggdraw.Pen(node.leave_color, 1)
			b = aggdraw.Brush(node.leave_color,255)
			d.ellipse((349+node._absolut_position[0]-1.4*node.leave_size,73+node._absolut_position[1]-1.4*node.leave_size,
				349+node._absolut_position[0]+0.6*node.leave_size,73+node._absolut_position[1]+0.6*node.leave_size),p,b)
			d.flush()
		paint_leaves(node, [offset[0]+node.position[0],
			offset[1]+node.position[1]], im)


for i in range(0,200):
	node.shrink(None)
	im = Image.open("./base.png")#Image.new("RGBA",(1280,720),"white")
	paint_branches(node,[0,0], im)
	paint_leaves(node,[0,0], im)
	im.save("./images/image{}.png".format(199-i),"png")

#im = Image.new("L",(1280,720),"white")
#func(node,[0,0], im ,0)
#im.show()
