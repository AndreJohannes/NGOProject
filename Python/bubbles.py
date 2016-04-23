from PIL import Image
import aggdraw

im = Image.new("RGBA",(1280,720),"white")


circles=[[1280/2,10]]

counter = 0
size = 10
lm =15
for i in range(0,240):
	im.paste("white",(0,0,1280,720))
	d = aggdraw.Draw(im)
	p = aggdraw.Pen("black", 2.5)
	counter+=1
	if (counter>lm):
		size+=10
		lm+=4
		circles.append([1280/2,size])
		counter=0
	for circle in circles:
		pos = circle[0]
		rad = circle[1]
		d.ellipse((pos-rad, 360-rad, pos+rad, 360+rad), p)
		circle[0]+= -5
	d.flush()
	im.save("bubble"+str(i)+".png","png")

world = circles.pop()
counter =0;
for i in range(240,340):
	im.paste("white",(0,0,1280,720))
	d = aggdraw.Draw(im)
	p = aggdraw.Pen("black", max(2.5-counter/3.,0))
	for circle in circles:
		pos = circle[0]
		rad = circle[1]
		d.ellipse((pos-rad, 360-rad, pos+rad, 360+rad), p)
		circle[0]+= -5
	pos = world[0]
	rad = world[1]
	world[1]+= 5
	p = aggdraw.Pen("black", 2.5+counter)
	counter +=0.1;
	d.ellipse((pos-rad, 360-rad, pos+rad, 360+rad),p)	
	d.flush()
	im.save("bubble"+str(i)+".png","png")