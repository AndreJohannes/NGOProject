import xml.etree.ElementTree as ET
from PIL import Image
import aggdraw

class Node:

	def __init__(self, parent, absolut_position):
		self.parent = parent
		self.children = []
		self._absolut_position = absolut_position
		if parent is None:
			self.position = absolut_position
		else:
			self.position = [absolut_position[0]-parent._absolut_position[0],
				absolut_position[1]-parent._absolut_position[1]]

	def addChild(self, absolut_position):
		node = Node(self, absolut_position)
		self.children.append(node)
		return node

def addChildrenFromXML(parent, node):
	for element in parent.getchildren():
		_node = node.addChild([int(element.attrib["pos_x"]),int(element.attrib["pos_y"])])
		addChildrenFromXML(element, _node) 

root = ET.parse("tree.xml").getroot()
node = Node(None, [329,428])
addChildrenFromXML(root, node)

im = Image.new("L",(1280,720),"white")
def func(parent, offset):
	for node in parent.children:
		d = aggdraw.Draw(im)
		p = aggdraw.Pen("black", 2.5)
		#d.line((offset[0],offset[1],
		#	offset[0]+node.position[0],offset[1]+node.position[1]),p)
		d.line((parent._absolut_position[0],parent._absolut_position[1],
			node._absolut_position[0],node._absolut_position[1]),p)
		d.flush()
		func(node, [offset[0]+node.position[0],offset[1]+node.position[1]])

func(node,[0,0])

im.show()



