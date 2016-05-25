from PIL import Image
import xml.etree.ElementTree as ET
from svg.path import parse_path
import aggdraw
import random

class svgParse:

	def __init__(self, filename):
		root = ET.parse(filename).getroot()
		paths=[]
		for element in root.getchildren():
			if str.endswith(element.tag,"path"):
				paths.append(parse_path(element.attrib["d"]))

		self.paths = [] 

		for path in paths:
			a_path = aggdraw.Path()
			self.paths.append(a_path)
			for line in path:
				x1 = line.start.real
				y1 = line.start.imag
				x2 = line.end.real
				y2 = line.end.imag

				a_path.moveto(x1, y1)
				a_path.lineto(x2, y2) 


	def get_path(self, idx):
		retArray = []
		coords = self.paths[idx].coords()
		for i in range(0,len(coords)/2):
			retArray.append([coords[2*i],coords[2*i+1]])
		return retArray	

#parser = svgParse("./Hidalgo.svg")
#area = parser.get_path(2)

#image = Image.new("RGBA",(200,200),"w"./Hidalgo.svg"hite")
#canvas = aggdraw.Draw(image)
#pen  = aggdraw.Pen("black", 1)
#brush = aggdraw.Brush("brown",255)
#path = []
#for coord in area:
#	path.append(coord[0])
#	path.append(coord[1])
#canvas.polygon(path,pen, brush)
#canvas.flush()
#image.show()

