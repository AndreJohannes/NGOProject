from PIL import Image
from PIL import ImageDraw
from PIL import ImageOps   
import aggdraw
from Python.phrases import Phrases
import Python.tools as Tools
import Python.transitions as Transitions

im = Image.open("./base2.png")
im = im.convert("L")
im = ImageOps.invert(im)

istart = 1500

production = not False
iOffset = 2806+istart if production else istart

for i in range(0, 150):
	base = Image.new("RGBA",(1280,720),"white")
	im = Image.open("../BuildTree/images/image{}.png".format(min(i-0, 199))) 
	#im = im.convert("L")
	#im = ImageOps.invert(im)
	base.paste(im,(0,0))
	base.paste("white",(0,0),Image.new("L",(1280,720), max(0,190-i*5)))
	color = 255.*(1-(i-0)/99.)
	textMask = Phrases.getPhrase29(1000)
	textMask2 = Image.new("L",textMask.size,"black")
	textMask2.paste((color),(0,0),textMask)
	base.paste("black",(50, 200-i),textMask2)
	d = ImageDraw.Draw(base)
	d.text((0,0),str(i + iOffset),"black")
	print "saving image:" , i + iOffset 
	base.save("./images/image" + str(i+iOffset) + ".png","png") if not production else base.save("../Movie/images/image" + str(i+iOffset) + ".png","png")	

iOffset += 150

for i in range(0, 115):
	base = Image.new("RGBA",(1280,720),"white")
	im = Image.open("../BuildTree/images/image{}.png".format(150)) 
	#im = im.convert("L")
	#im = ImageOps.invert(im)
	base.paste(im,(0,0))
	textMask = Phrases.getPhrase30(i)
	base.paste("black",(50, 300-i),textMask)
	d = ImageDraw.Draw(base)
	d.text((0,0),str(i + iOffset),"black")
	print "saving image:" , i + iOffset 
	base.save("./images/image" + str(i+iOffset) + ".png","png") if not production else base.save("../Movie/images/image" + str(i+iOffset) + ".png","png")	

iOffset += 115
for i in range(0, 90):
	base = Image.new("RGBA",(1280,720),"white")
	im = Image.open("../BuildTree/images/image{}.png".format(min(i+150, 199))) 
	#im = im.convert("L")
	#im = ImageOps.invert(im)
	base.paste(im,(0,0))
	color = 255.*(1-(i-0)/99.)
	textMask = Phrases.getPhrase30(1000)
	textMask2 = Image.new("L",textMask.size,"black")
	textMask2.paste((color),(0,0),textMask)
	base.paste("black",(50, 185-i),textMask2)
	d = ImageDraw.Draw(base)
	d.text((0,0),str(i + iOffset),"black")
	print "saving image:" , i + iOffset 
	base.save("./images/image" + str(i+iOffset) + ".png","png") if not production else base.save("../Movie/images/image" + str(i+iOffset) + ".png","png")	

iOffset += 90
def callback(im, i):
	d = ImageDraw.Draw(im)
	d.text((0,0),str(i+iOffset),"black")
	print "saving image:" , i + iOffset
	im.save("./images/image" + str(i+iOffset) + ".png","png") if not production else im.save("../Movie/images/image" + str(i+iOffset) + ".png","png")
Transitions.pageflip(base, Image.open("./base5.png"), 30, callback)





