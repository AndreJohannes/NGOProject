from PIL import Image
import xml.etree.ElementTree as ET
from svg.path import parse_path
import aggdraw
import random
from Python.phrases import Phrases

root = ET.parse("branch.jpg.svg").getroot()
paths=[]
for element in root.getchildren():
	if str.endswith(element.tag,"path"):
		paths.append(parse_path(element.attrib["d"]))

base = Image.new("RGB",(1280,720), "white")
canvas = aggdraw.Draw(base)
pen  = aggdraw.Pen("black", 1)
brush = aggdraw.Brush("brown",255)

for leave in paths:
		
	path = aggdraw.Path()

	for line in leave:
		x1 = line.start.real
		y1 = line.start.imag
		x2 = line.end.real
		y2 = line.end.imag

		path.moveto(150+1.5*x1, 1.5*y1)
		path.lineto(150+1.5*x2, 1.5*y2) 

	canvas.polygon(path.coords(),pen, brush)

canvas.flush()


root = ET.parse("leavesonbranch.svg").getroot()
paths = []

for element in root.getchildren():
	if str.endswith(element.tag,"path"):
		paths.append(parse_path(element.attrib["d"]))


colors =[]
colors.append((116,167,40))
colors.append((116,134,40))
colors.append((128,0,0))
colors.append((116,128,40))
colors.append((0,128,0))
colors.append((144,128,40))
colors.append((116,128,40))
colors.append((42,132,17))
colors.append((42,115,54))
colors.append((51,72,56))
colors.append((116,128,40))
colors.append((144,128,40))

ret = {}
def getRetardation(i):
	if not ret.has_key(i):
		ret[i] = random.randint(0,100)
	return ret[i]

for i in range(0, 200):

	im = base.copy()#Image.new("RGB",(1280,720), "white")
	canvas = aggdraw.Draw(im)
	pen  = aggdraw.Pen("black", 1)

	leave_count = 0
	for leave in paths:
		leave_count += 1
		size = max(0,min((i-getRetardation(leave_count))/99.,1))
		path = aggdraw.Path()

		x_start = leave[0].start.real
		y_start = leave[0].start.imag

		brush = aggdraw.Brush(colors[leave_count],255)

		for line in leave:
			x1 = line.start.real
			y1 = line.start.imag
			x2 = line.end.real
			y2 = line.end.imag

			x1 = x_start + size*(x1-x_start)
 	  		x2 = x_start + size*(x2-x_start)
			y1 = y_start + size*(y1-y_start)
 	  		y2 = y_start + size*(y2-y_start)

			path.moveto(150+1.5*x1, 1.5*y1)
			path.lineto(150+1.5*x2, 1.5*y2) 

		canvas.polygon(path.coords(),pen, brush)
	
	canvas.flush()
	#textMask = Phrases.getPhrase32(1000)
	#im.paste("black",(64, 445),textMask)
	im.save("./images/preps/image{}.png".format(i),"png")
