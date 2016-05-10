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

istart = 1280

production = not False
iOffset = 2806+istart if production else istart

def callback(im, i):
	d = ImageDraw.Draw(im)
	d.text((0,0),str(i+iOffset),"black")
	print "saving image:" , i + iOffset
	im.save("./images/image" + str(i+iOffset) + ".png","png") if not production else im.save("../Movie/images/image" + str(i+iOffset) + ".png","png")
im1 = Image.new("RGBA",(1280,720),"white")
im1.paste((190,190,190),(0,0),ImageOps.invert(Image.open("./base3.png").convert("L")))
Transitions.horizontalflip(im1, Image.open("./base4.png"), 20, callback)

iOffset += 20

for i in range(0, 100):
	base = Image.new("RGBA",(1280,720),"white")
	if (i>50):
		im = Image.open("../BuildFoundation/images/watering/image{:02d}.png".format(min(i-50, 41))) 
   		im = im.convert("L")
		im = ImageOps.invert(im)
	else:
		im = Image.open("../BuildFoundation/images/seeding/image{}.png".format(min(i-0, 33))) 
		im = im.convert("L")
		im = ImageOps.invert(im)
	base.paste("black",(0,46),im)

	d = ImageDraw.Draw(base)
	d.text((0,0),str(i+iOffset),"black")
	print "saving image:" , i + iOffset 
	base.save("./images/image" + str(i+iOffset) + ".png","png") if not production else base.save("../Movie/images/image" + str(i+iOffset) + ".png","png")

iOffset += 100
for i in range(0, 100):
	im = Image.open("./base4.png")
	im = im.convert("L")
	im = ImageOps.invert(im)
	base = Image.new("RGBA",(1280,720),"white")
	color = min(i*5,190) 
	base.paste((color,color,color),(0,0),im)

	textMask = Phrases.getPhrase29(i)
	base.paste("black",(50, 300-i),textMask)

	d = ImageDraw.Draw(base)
	d.text((0,0),str(i + iOffset),"black")
	print "saving image:" , i + iOffset 
	base.save("./images/image" + str(i+iOffset) + ".png","png") if not production else base.save("../Movie/images/image" + str(i+iOffset) + ".png","png")

iOffset += 100
for i in range(0, 155):
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

