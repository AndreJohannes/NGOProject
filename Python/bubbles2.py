from PIL import Image
import aggdraw
import math

im = Image.new("RGBA",(1280,720),"white")

inicio = [190,700,10]

circles=[list(inicio)]

counter = 0
lm =25
for i in range(0,120):
	im.paste("white",(0,0,1280,720))
	d = aggdraw.Draw(im)
	p = aggdraw.Pen("black", 2.5)
	counter += 1
	if (counter>lm):
		lm += 0
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
	#im.save("bubble"+str(i)+".png","png")

world = circles[3]
circles.remove(world)
dRadius = 0;
counter =0;
frac = 0;
for i in range(120,240):
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
	pos_x = (1-frac)*world[0]+(frac)*1280/2.
	pos_y = (1-frac)*world[1]+(frac)*720/2.
	radius = world[2]
	p = aggdraw.Pen("black", 2.5+counter/30.)
	world[0]+= 1.25 + radius/10
	world[1]-= 0.67 + radius*radius/500
	world[2]+= .4
	dRadius += 1.2
	frac = counter*counter/(120.*120.)

	print frac
	counter +=1;
	d.ellipse((pos_x-radius-dRadius, pos_y-radius-dRadius, pos_x+radius+dRadius, pos_y+radius+dRadius),p)	
	d.flush()
	im.save("bubble"+str(i)+".png","png")