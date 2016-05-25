from PIL import Image
import xml.etree.ElementTree as ET
from svg.path import parse_path
import aggdraw
import random
from Python.phrases import Phrases

root = ET.parse("branch2.svg").getroot()
paths=[]
for element in root.getchildren():
	if str.endswith(element.tag,"path"):
		paths.append(parse_path(element.attrib["d"]))

base = Image.new("RGBA",(1280,720))
canvas = aggdraw.Draw(base)
pen  = aggdraw.Pen((123, 79, 2), 1)
brush = aggdraw.Brush((143, 89, 2),255)

for leave in paths:
		
	path = aggdraw.Path()

	for line in leave:
		x1 = line.start.real
		y1 = line.start.imag
		x2 = line.end.real
		y2 = line.end.imag

		path.moveto(150+1.3*x1, 1.3*y1-250)
		path.lineto(150+1.3*x2, 1.3*y2-250) 

	canvas.polygon(path.coords(),pen, brush)

canvas.flush()


root = ET.parse("leavesonbranch2.svg").getroot()
paths = []

for element in root.getchildren():
	if str.endswith(element.tag,"path"):
		paths.append(parse_path(element.attrib["d"]))

paths.reverse()

colors =[]
colors.append((0,228,0))
colors.append((100,252,12))
colors.append((138, 226, 52))
colors.append((124,232,0))

ret = {}
def getRetardation(i):
	if not ret.has_key(i):
		ret[i] = random.randint(0,100)
	return ret[i]

for i in range(0, 200):

	im = base.copy()#Image.new("RGB",(1280,720), "white")

	canvas = aggdraw.Draw(im)
	pen  = aggdraw.Pen("green", 1)

	leave_count = 0
	for leave in paths:
		size = max(0,min((i-getRetardation(leave_count))/99.,1.0))
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

			path.moveto(150+1.3*x1, 1.3*y1-250)
			path.lineto(150+1.3*x2, 1.3*y2-250) 

		canvas.polygon(path.coords(),pen, brush)
		leave_count += 1
	canvas.flush()

	size = max(0,min((i-getRetardation(0))/99.,1.0))
	text = Image.open("./text1.png")
	text = text.resize((int(size*text.size[0]), int(size*text.size[1])), Image.BICUBIC)
	im.paste(text,(349+int(152*(1-size)), 103),text)

	size = max(0,min((i-getRetardation(3))/99.,1.0))
	text = Image.open("./text2.png")
	text = text.resize((int(size*text.size[0]), int(size*text.size[1])), Image.BICUBIC)
	im.paste(text,(433+int(190*(1-size)), 344),text)

	size = max(0,min((i-getRetardation(2))/99.,1.0))
	text = Image.open("./text3.png")
	text = text.resize((int(size*text.size[0]), int(size*text.size[1])), Image.BICUBIC)
	im.paste(text,(691, 425),text)

	size = max(0,min((i-getRetardation(1))/99.,1.0))
	text = Image.open("./text4.png")
	text = text.resize((int(size*text.size[0]), int(size*text.size[1])), Image.BICUBIC)
	im.paste(text,(632, 72 +int(109*(1-size))),text)


	#textMask = Phrases.getPhrase32(1000)
	#im.paste("black",(64, 445),textMask)
	im.save("./images/preps/image{}.png".format(i),"png")

	#text1 349 / 103
	#text2  433 / 344
	#text3  691 / 425
	#text4  632 / 72 (109)