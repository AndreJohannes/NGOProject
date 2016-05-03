from PIL import Image
from PIL import ImageDraw
import aggdraw
import math

iOffset = 396

for i in range(0,30):
	image = Image.open("./images/wall"+ "{:02d}".format(i) +".png")
	image = image.convert("RGBA");
	d = aggdraw.Draw(image)
	p = aggdraw.Pen("black", 8.46666)
	d.ellipse((640-315,596,640+315,596),p)
	d.flush()
	image1 = image.copy()
	d = ImageDraw.Draw(image1)
	d.text((0,0),str(2*i+iOffset),"black")
	image1.save("../Movie/images/image" + str(iOffset+2*i) +".png")
	d = ImageDraw.Draw(image)
	d.text((0,0),str(2*i+iOffset+1),"black")
	image.save("../Movie/images/image" + str(iOffset+2*i+1) +".png")