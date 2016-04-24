from PIL import Image
from PIL import ImageDraw
import aggdraw
import math

ioffset = 396

for i in range(0,30):
	image = Image.open("./images/wall"+ "{:02d}".format(i) +".png")
	image = image.convert("RGBA");
	d = aggdraw.Draw(image)
	p = aggdraw.Pen("black", 8.46666)
	d.ellipse((640-315,596,640+315,596),p)
	d.flush()
	image.save("../Movie/image" + str(ioffset+2*i) +".png")
	image.save("../Movie/image" + str(ioffset+2*i+1) +".png")