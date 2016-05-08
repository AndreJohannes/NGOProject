from PIL import Image
from PIL import ImageDraw
import aggdraw
from Python.phrases import Phrases
import Python.tools as Tools
import Python.transitions as Transitions


production = not False
iOffset = 2046+270 if production else 270

dOffset = 80
def callback(im, i):
	d = ImageDraw.Draw(im)
	d.text((0,0),str(i+iOffset),"black")
	print "saving image:" , i + iOffset
	im.save("./images/image" + str(i+iOffset) + ".png","png") if not production else im.save("../Movie/images/image" + str(i+iOffset) + ".png","png")
Transitions.blender(Image.open("./hidalgo.png").convert("RGBA"), 
	Image.open("./mezquital.png").convert("RGBA"), dOffset, callback)
iOffset += dOffset
Transitions.blender(Image.open("./mezquital.png").convert("RGBA"), 
	Image.open("./huasteca.png").convert("RGBA"), dOffset, callback)
iOffset += dOffset
Transitions.blender(Image.open("./huasteca.png").convert("RGBA"), 
	Image.open("./otomi.png").convert("RGBA"), dOffset, callback)
