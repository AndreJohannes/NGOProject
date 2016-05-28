import xml.etree.ElementTree as ET
from PIL import Image
import aggdraw
import math
import random 
import tree_parser

root = ET.parse("tree.xml").getroot()
node = tree_parser.Node(None, [329,420],1, False)
tree_parser.addChildrenFromXML(root, node)

def paint_branches(parent, offset, im):
	for node in parent.children:
		d = aggdraw.Draw(im)
		p = aggdraw.Pen("black", node.girth)
		d.line((1.3*parent._absolut_position[0]+349,1.3*parent._absolut_position[1]+96
			,1.3*node._absolut_position[0]+349,1.3*node._absolut_position[1]+96),p)
		d.flush()
		paint_branches(node, [offset[0]+node.position[0],
			offset[1]+node.position[1]], im)

def paint_leaves(parent, offset, im):
	for node in parent.children:
		if node.has_leave:
			d = aggdraw.Draw(im)
			for i in range(0,66):
				color = (random.randint(40,180), random.randint(120,250), random.randint(0,50))
				p = aggdraw.Pen(color, 1)
				b = aggdraw.Brush(color,255)
				dx = random.randint(-3*int(node.leave_size), 3*int(node.leave_size))
				dy = random.randint(-3*int(node.leave_size), 3*int(node.leave_size))
				d.ellipse((dx+349+1.3*node._absolut_position[0]-5,dy+96+1.3*node._absolut_position[1]-5,
					dx+349+1.3*node._absolut_position[0]+5,dy+96+1.3*node._absolut_position[1]+5),p,b)
			d.flush()
		paint_leaves(node, [offset[0]+node.position[0],
			offset[1]+node.position[1]], im)


im = Image.new("RGBA",(1280,720),"white")
paint_branches(node,[0,0], im)
paint_leaves(node,[0,0], im)
im.save("./big/image.png","png")

#im = Image.new("L",(1280,720),"white")
#func(node,[0,0], im ,0)
#im.show()
