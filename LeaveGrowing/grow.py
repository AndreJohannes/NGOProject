from PIL import Image
import xml.etree.ElementTree as ET
from svg.path import parse_path
import aggdraw
import random
from Python.phrases import Phrases

for i in range(0, 300):

	im = Image.open("./images/preps/image{}.png".format(min(i,199)))

	if i<110:
		textMask = Phrases.getPhrase31(i)
		im.paste("black",(50, 320-i),textMask)
	else:
		color = 255.*(1-(i-110)/99.)
		textMask = Phrases.getPhrase31(1000)
		textMask2 = Image.new("L",textMask.size,"black")
		textMask2.paste((color),(0,0),textMask)
		im.paste("black",(50, 320-i),textMask2)


	textMask = Phrases.getPhrase34(max(0,(i-130)/2))
	im.paste("black",(737, 426),textMask)

	textMask = Phrases.getPhrase35(max(0,(i-140)/2))
	im.paste("black",(428, 462),textMask)

	textMask = Phrases.getPhrase33(max(0,(i-160)/2))
	im.paste("black",(541, 127),textMask)

	textMask = Phrases.getPhrase32(max(0,(i-180)/2))
	im.paste("black",(224, 445),textMask)

	im.save("./images/image{}.png".format(i),"png")

