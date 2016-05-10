from PIL import Image
from PIL import ImageDraw
from PIL import ImageOps   
import aggdraw
from Python.phrases import Phrases
import Python.tools as Tools
import Python.transitions as Transitions


istart = 1872

production = not False
iOffset = 2806+istart if production else istart

for i in range(0,300):
	im = Image.open("../LeaveGrowing/images/image{}.png".format(i))

	d = ImageDraw.Draw(im)
	d.text((0,0),str(i + iOffset),"black")
	print "saving image:" , i + iOffset 
	im = im.convert("RGBA")
	im.save("./images/image" + str(i+iOffset) + ".png","png") if not production else im.save("../Movie/images/image" + str(i+iOffset) + ".png","png")	
