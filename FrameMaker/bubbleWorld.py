import aggdraw
from PIL import Image

class bubble:

	def __init__(self,start, fading, length):
		self.startTime = start
		self.stopTime = start + length
		pos_x = 190
		pos_y = 700
		radius = 10
		pen_size = 2.5
		self.bubbles = [[pos_x, pos_y, radius, pen_size]]
		for i in range(1, length):
			pos_x += 1.25 + radius/10
			pos_y -= 0.67 + radius*radius/500
			radius += 0.4
			if i>=fading:
				pen_size = max(0,2.5-(i-fading)/30.)
			self.bubbles.append([pos_x, pos_y, radius, pen_size])

	def draw(self, frame, image):
		if(frame < self.startTime or frame >= self.stopTime):
 			return
 		pos_x = self.bubbles[frame-self.startTime][0]
 		pos_y = self.bubbles[frame-self.startTime][1]
 		radius = self.bubbles[frame-self.startTime][2]
 		pen_size = self.bubbles[frame-self.startTime][3]
 		d = aggdraw.Draw(image)
		p = aggdraw.Pen("black", pen_size)
		d.ellipse((pos_x-radius, pos_y-radius, pos_x+radius, pos_y+radius), p)
		d.flush()

class worldBubble:

	def __init__(self,start, length):
		self.startTime = start
		self.stopTime = start + length
		self.world = Image.open("../Images/world.png")
		pos_x1 = 322.87
		pos_y1 = 640.1548
		radius1 = 27.199999999999964
		radius2 = 1.2
		pen_size = 2.5
		frac = 0
		self.bubbles = [[pos_x1, pos_y1, radius1 + radius2, pen_size]]
		for i in range(1, length):
			pos_x1 += 1.25 + radius1/10
			pos_y1 -= 0.67 + radius1*radius1/500
			radius1 += 0.4 
			radius2 += 1.2
			pos_x = (1-frac)*pos_x1+(frac)*1280/2.
			pos_y = (1-frac)*pos_y1+(frac)*720/2.
			radius = min(radius2 + radius1,315);
			frac = min(1,i*i/(120.*120.))
			self.bubbles.append([pos_x, pos_y, radius, pen_size + i/30.])

	def draw(self, frame, image):
		if(frame < self.startTime or frame >= self.stopTime):
 			return
 		pos_x = self.bubbles[frame-self.startTime][0]
 		pos_y = self.bubbles[frame-self.startTime][1]
 		radius = self.bubbles[frame-self.startTime][2]
 		pen_size = self.bubbles[frame-self.startTime][3]
 		world_rsz = self.world.resize((int(2*radius),int(2*radius)),Image.BILINEAR)
		color = max(255-(frame-self.startTime)*2,0)
		image.paste((color,color,color),(int(pos_x-radius), int(pos_y-radius)),world_rsz) 		
		d = aggdraw.Draw(image)
		p = aggdraw.Pen("black", pen_size)
		d.ellipse((int(pos_x-radius), int(pos_y-radius), int(pos_x+radius), int(pos_y+radius)), p)
		d.flush()
