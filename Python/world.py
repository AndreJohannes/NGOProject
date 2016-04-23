from PIL import Image
from PIL import ImageDraw
import aggdraw
import math

im = Image.new("RGBA",(1280,720),"white")

coastLine = Image.open("../Images/world.png")

iOffset = 300

for i in range(0,80):
	im.paste("white",(0,0,1280,720))
	radius_x = 315
	radius_y = 315

	radius_y = int(315 * (1-math.sin(math.pi/2.*(i/79.))))
	offset_y = int(0.75*(315-radius_y))

	CLresized=coastLine.resize((2*radius_x,2*radius_y),Image.BILINEAR)
	im.paste((0,0,0),(640-radius_x,360-radius_y+offset_y),CLresized)
	d = aggdraw.Draw(im)
	p = aggdraw.Pen("black", 8.46666)
	d.ellipse((640-radius_x, 360-radius_y+offset_y, 640+radius_x, 360+radius_y+offset_y), p)
	d.flush();
	im.save("./images/image"+str(i+iOffset)+".png","png")


