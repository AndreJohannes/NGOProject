from PIL import Image
from PIL import ImageDraw
import aggdraw
from Python.phrases import Phrases
import Python.tools as Tools
import Python.transitions as Transitions


production = not False
iOffset = 2046 if production else 0

dOffset = 170
for i in range(0, dOffset):

	im = Image.open("./images/preps/image{}.png".format(min(i, 169)))

	textMask = Phrases.getPhrase24(i)
	im.paste("black",(50, 280),textMask)

	d = ImageDraw.Draw(im)
	d.text((0,0),str(i+iOffset),"black")
	print "saving image:" , i + iOffset 
	im.save("./images/image" + str(i+iOffset) + ".png","png") if not production else im.save("../Movie/images/image" + str(i+iOffset) + ".png","png")


iOffset += dOffset

for i in range(0, 100):

	im = Image.open("./hidalgo.png")

	color = 255.*(1-i/99.)

	textMask = Phrases.getPhrase24(170+i)
	textMask2 = Image.new("L",textMask.size,"black")
	textMask2.paste((color),(0,0),textMask)
	im.paste("black",(50, 280),textMask2)

	d = ImageDraw.Draw(im)
	d.text((0,0),str(i+iOffset),"black")
	print "saving image:" , i + iOffset
	im.save("./images/image" + str(i+iOffset) + ".png","png") if not production else im.save("../Movie/images/image" + str(i+iOffset) + ".png","png")