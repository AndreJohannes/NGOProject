from PIL import Image
from PIL import ImageDraw
import aggdraw
import math
import random
from Python.phrases import Phrases
from Python.flags import Flags
import Python.tools as Tools
import Python.transitions as Transitions

production =  True
iOffset = 6060 if production else 0

base = Image.open("./base.png")

def callback(im, i):
	d = ImageDraw.Draw(im)
	d.text((0,0),str(i+iOffset),"black")
	print "saving image:" , i + iOffset
	im.save("./images/image" + str(i+iOffset) + ".png","png") if not production else im.save("../Movie/images/image" + str(i+iOffset) + ".png","png")
Transitions.blender(Image.open("./base2.png").convert("RGBA"), base, 30, callback)

iOffset += 30

for i in range(0,500):
	im = Image.new("RGBA",(1280,720),"white")
	im.paste(base,(0,0))
	textMask = Phrases.getPhrase53(2*i)
	im.paste("black",(370, 300-2*i),textMask)
	callback(im, i)