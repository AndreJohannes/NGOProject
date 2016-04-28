from PIL import Image
from PIL import ImageDraw
import aggdraw
import math
import random
from Python.phrases import Phrases
from Python.flags import Flags
import Python.tools as Tools


production = True
iOffset = 1846 if production else 0

base = Image.open("./base.png")

for i in range(0,200):
	im = Image.new("RGBA",(1280,720),"white")
	im.paste(base,(0,0))
	textMask = Phrases.getPhrase26(i)
	im.paste("black",(400, 50),textMask)
	textMask = Phrases.getPhrase27(i-80)
	im.paste("black",(400, 600),textMask)
	d = ImageDraw.Draw(im)
	d.text((0,0),str(i+iOffset),"black")
	print "saving image:" , i 
	im.save("./images/image" + str(i+iOffset) + ".png","png") if not production else im.save("../Movie/image" + str(i+iOffset) + ".png","png")

