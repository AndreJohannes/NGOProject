from PIL import Image
from PIL import ImageDraw
import aggdraw
import math

production = not False

im = Image.new("RGBA",(1280,720),"white")

coastLines = Image.open("../Images/world.png")

inicio = [190,700,10]

circles=[list(inicio)]

counter = 0
umbral = 25
for i in range(0,120):
	im.paste("white",(0,0,1280,720))
	d = aggdraw.Draw(im)
	p = aggdraw.Pen("black", 2.5)
	counter += 1
	if (counter>umbral):
		circles.append(list(inicio))
		counter = 0
	for circle in circles:
		pos_x = circle[0]
		pos_y = circle[1]
		radius = circle[2]
		d.ellipse((pos_x-radius, pos_y-radius, pos_x+radius, pos_y+radius), p)
		circle[0]+= 1.25 + radius/10
		circle[1]-= 0.67 + radius*radius/500
		circle[2]+=.4
	d.flush()
	d = ImageDraw.Draw(im)
	d.text((0,0),str(i),"black")
	im.save("./images/image" + str(i) + ".png","png") if not production else im.save("../Movie/images/image" + str(i) + ".png","png")

world = circles[3]
circles.remove(world)
dRadius = 0;
counter =0;
frac = 0;
for i in range(120,300):
	im.paste("white",(0,0,1280,720))
	d = aggdraw.Draw(im)
	p = aggdraw.Pen("black", max(2.5-counter/30.,0))
	for circle in circles:
		pos_x = circle[0]
		pos_y = circle[1]
		radius = circle[2]
		d.ellipse((pos_x-radius, pos_y-radius, pos_x+radius, pos_y+radius), p)
		circle[0]+= 1.25 + radius/10
		circle[1]-= 0.67 + radius*radius/500
		circle[2]+=.4
	d.flush()
	pos_x = (1-frac)*world[0]+(frac)*1280/2.
	pos_y = (1-frac)*world[1]+(frac)*720/2.
	world[0]+= 1.25 + world[2]/10
	world[1]-= 0.67 + world[2]*world[2]/500
	world[2]+= .4
	dRadius += 1.2
	radius = min(dRadius + world[2],315);
	frac = min(1,counter*counter/(120.*120.))
	CLresized = coastLines.resize((int(2*radius),int(2*radius)),Image.BILINEAR)
	color = max(255-counter*2,0)
	im.paste((color,color,color),(int(pos_x-radius), int(pos_y-radius)),CLresized)
	d = aggdraw.Draw(im)
	p = aggdraw.Pen("black", 2.5+counter/30.)
	counter +=1;
	d.ellipse((int(pos_x-radius), int(pos_y-radius), int(pos_x+radius), int(pos_y+radius)),p)	
	d.flush()
	d = ImageDraw.Draw(im)
	d.text((0,0),str(i+120),"black")
	im.save("./images/image" + str(i) + ".png","png") if not production else im.save("../Movie/images/image" + str(i) + ".png","png")
	
world = [pos_x, pos_y, radius]

print world
