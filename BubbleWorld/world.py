from PIL import Image
from PIL import ImageDraw
import aggdraw
import math

im = Image.new("RGBA",(1280,720),"white")

title = Image.open("./title.png")
coastLine = Image.open("../Images/world.png")

iOffset = 300

for i in range(0, 80):
	im.paste("white",(0, 0, 1280, 720))
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

	mask = Image.new("L",title.size,max(255-5*i,0))
	im.paste(title,(0,0),mask)

	d = ImageDraw.Draw(im)
	d.text((0,0),str(i+iOffset),"black")

	im.save("./images/image"+str(i+iOffset)+".png","png")

iOffset = 380
for i in range(0,80):
	im.paste("white",(0,0,1280,720))
	d = aggdraw.Draw(im)
	p = aggdraw.Pen("black", 8.46666)
	d.ellipse((640-radius_x, 360-radius_y+offset_y, 640+radius_x, 360+radius_y+offset_y), p)
	d.flush();

	d = ImageDraw.Draw(im)
	d.text((0,0),str(i+iOffset),"black")

	im.save("./images/image"+str(i+iOffset)+".png","png")




