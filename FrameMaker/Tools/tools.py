from PIL import Image
from PIL import ImageDraw
import aggdraw
import math
import random
import flags as Flags

class RCRectengular:
	@staticmethod
	def draw(d, rec, radius, p, b = None):
		if b==None:
			b = aggdraw.Brush("white",255);
		d.rectangle((rec[0]+radius,rec[1],rec[2]-radius,rec[3]),None, b)
		d.rectangle((rec[0],rec[1]+radius,rec[0]+radius,rec[3]-radius),None, b)
		d.rectangle((rec[2],rec[1]+radius,rec[2]-radius,rec[3]-radius),None, b)
		d.pieslice((rec[0],rec[1],rec[0]+2*radius,rec[1]+2*radius),90,180,None, b)
		d.pieslice((rec[2]-2*radius,rec[1],rec[2],rec[1]+2*radius),0,90,None, b)
		d.pieslice((rec[0],rec[3]-2*radius,rec[0]+2*radius,rec[3]),180,270,None, b)
		d.pieslice((rec[2]-2*radius,rec[3]-2*radius,rec[2],rec[3]),270,360,None, b)
		d.line((rec[0]+radius,rec[1],rec[2]-radius,rec[1]),p)
		d.line((rec[0]+radius,rec[3],rec[2]-radius,rec[3]),p)
		d.line((rec[0],rec[1]+radius,rec[0],rec[3]-radius),p)
		d.line((rec[2],rec[1]+radius,rec[2],rec[3]-radius),p)
		d.arc((rec[0],rec[1],rec[0]+2*radius,rec[1]+2*radius),90,180,p)
		d.arc((rec[2]-2*radius,rec[1],rec[2],rec[1]+2*radius),0,90,p)
		d.arc((rec[0],rec[3]-2*radius,rec[0]+2*radius,rec[3]),180,270,p)
		d.arc((rec[2]-2*radius,rec[3]-2*radius,rec[2],rec[3]),270,360,p)

class TimedBubble:
	def __init__(self, pos_x, pos_y, radius, startTime, 
		duration):
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.radius = radius
		self.startTime = startTime
		self.duration = duration
		self.stopTime = startTime + duration + 1 

	def draw(self,frame, image):
		if frame < self.startTime or frame >= self.stopTime:
			return
		d = aggdraw.Draw(image)
		p = aggdraw.Pen("black", 2.5)
		idx = frame - self.startTime
		color = int(255-(255*idx)/self.duration) 
		p = aggdraw.Pen((color, color, color), 2.5)
		d.ellipse((self.pos_x-self.radius, self.pos_y-self.radius, 
			self.pos_x+self.radius,self.pos_y+self.radius), p)
		d.flush()

class MorphingTextBox:
	
	def __init__(self, image, pos_x, pos_y, radius, startTime, hover = False):
		self.image = image
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.radius = radius
		self.startTime = startTime
		self.randomShift = random.randint(-10,10)
		self.hover = hover

	def draw(self, frame, image, b = None):
		if frame < self.startTime: 
			return 
		if b==None:
			b = aggdraw.Brush("white",255)
		idx = frame  - self.startTime
		y = int(self.pos_y + .2*(idx)) if self.hover else self.pos_y - 2*idx
		x = self.pos_x - 2*self.randomShift*math.sqrt((idx))
		radius = int(max(self.radius - 2*idx / 2.,5))
		hdx = min(int(self.radius + 8*idx / 2.),(self.image.size[0]+radius)/2)
		hdy = min(int(self.radius + 8*idx / 4.),(self.image.size[1]+radius)/2)
		d = aggdraw.Draw(image)
		p = aggdraw.Pen("black", 2.5)
		RCRectengular.draw(d, (x - hdx, y - hdy , x + hdx , y + hdy), radius, p, b)	
		d.flush()
		textbox = self.image.resize((2*hdx-2*radius,2*hdy-2*radius), Image.ANTIALIAS)
		textMask = Image.new("L",textbox.size,"black")
		color =  idx*10
		textMask.paste((color),(0,0),textbox)
		image.paste("black",(int(x)-hdx+radius,y-hdy+radius),textMask)

class TranscendingBubble:

	def __init__(self, image, pos_x, pos_y, radius, startTime):
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.radius = radius 
		self.startTime = startTime
		self.image = image

	def draw(self, frame, image):
		if(frame < self.startTime):
			return
		idx = frame - self.startTime
		radius = self.radius + 10 * idx  + 0.1* idx*idx
		mask = self.getMask(self.pos_x, self.pos_y, radius)
		image.paste(self.image, (0,0,1280,720), mask)
		d = aggdraw.Draw(image)
		p = aggdraw.Pen("black", 2.5)
		#b = aggdraw.Brush("white")
		d.ellipse((self.pos_x - radius, self.pos_y - radius, 
			self.pos_x + radius,self.pos_y + radius), p)
		d.flush()

	def getMask(self, pos_x, pos_y, radius):
		mask = Image.new("L",(1280,720),"black")
		d = aggdraw.Draw(mask)
		p = aggdraw.Pen("white", 2.5)
		b = aggdraw.Brush("white")
		d.ellipse((pos_x - radius, pos_y - radius, 
			pos_x + radius,pos_y + radius), p, b)
		d.flush()
		return mask

class MovingBubble:

	def __init__(self, pos_x, pos_y, radius, startTime, duration, left = False):
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.radius = radius
		self.startTime = startTime
		self.stopTime = startTime + duration
		self.to_right = not left


	def draw(self,frame, image):
		if frame < self.startTime:
			return
		if self.stopTime != None and self.stopTime < frame:
			return	
		idx = frame -self.startTime
		pos_x = self.pos_x + 5*idx if self.to_right else self.pos_x  - 5*idx
		pos_y = self.pos_y - 1*idx - 0.01*idx*idx 
		radius = self.radius + 0.5*idx	
		d = aggdraw.Draw(image)
		p = aggdraw.Pen("black", 2.5)
		color = max(0,int(255-(255*(idx))/10)) 
		p = aggdraw.Pen((int(color*248/255.), int(color*240/255.), int(color*118/255.)), 2.5);
		d.ellipse((pos_x-radius, pos_y-radius, 
			pos_x+radius,pos_y+radius), p)
		d.flush()

class RandomWalkTextBox:
	
	def __init__(self, image, pos_x, pos_y, radius, startTime):
		self.image = image
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.radius = radius
		self.startTime = startTime
		self.counter = 0
		self.randomShift = random.randint(-10,10)

	def draw(self, im):
		if self.counter < self.startTime: 
			return 
		dt = self.counter  - self.startTime
		y = self.pos_y - 2*(dt)
		x = self.pos_x - 2*self.randomShift*math.sqrt((dt))
		radius = int(max(self.radius - 2*dt / 2.,5))
		hdx = min(int(self.radius + 2*dt / 2.),(self.image.size[0]+radius)/2)
		hdy = min(int(self.radius + 2*dt / 4.),(self.image.size[1]+radius)/2)
		d = aggdraw.Draw(im)
		p = aggdraw.Pen("black", 2.5)
		RCRectengular.draw(d, (x - hdx, y - hdy , x + hdx , y + hdy), radius, p)	
		d.flush()
		textbox = self.image.resize((2*hdx-2*radius,2*hdy-2*radius), Image.ANTIALIAS)
		color = 255 - dt*5
		im.paste((color,color,color,256),(int(x)-hdx+radius,y-hdy+radius),textbox.convert("L"))

	def inc(self):
		self.counter += 1

class OneThought:

	def __init__(self, startTime, image, pos_x):
		self.bubble1 = TimedBubble(pos_x,358,10,startTime,30)
		self.bubble2 = TimedBubble(pos_x,318,15,startTime+10, 20)
		self.bubble3 = TimedBubble(pos_x,268,20,startTime+20, 10)
		self.rectangualar = MorphingTextBox(image, pos_x,268,20,startTime+30)
		self.brush = aggdraw.Brush((248,240,118),255)

	def draw(self, frame, image):
		self.bubble1.draw(frame, image)
		self.bubble2.draw(frame, image)
		self.bubble3.draw(frame, image)
		self.rectangualar.draw(frame, image, self.brush)

class OneFlag:

	def __init__(self, startTime, stopTime, name, pos_x, pos_y):
		flags = Flags.Flags() 
		self.image = flags.getFlag(name)
		self.startTime = startTime
		self.stopTime = stopTime + 1
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.counter = 0

	def draw(self, frame, image):
		if frame>=self.startTime and frame<self.stopTime:
			color = min(255,(frame-self.startTime)*30)
			mask = Image.new("L",self.image.size,(color))
			image.paste(self.image,(self.pos_x,self.pos_y),mask)

class ThoughtfulTransition:
	def __init__(self, startTime, image, pos_x):
		self.bubble1 = TimedBubble(pos_x,358,10,startTime,30)
		self.bubble2 = TimedBubble(pos_x,318,15,startTime+10,20)
		self.bubble3 = TimedBubble(pos_x,268,20,startTime+20,10)
		self.transcendingBubble = TranscendingBubble(image, pos_x, 268, 20, 
			startTime+30)

	def draw(self, frame, image):
		self.bubble1.draw(frame, image)
		self.bubble2.draw(frame, image)
		self.bubble3.draw(frame, image)
		self.transcendingBubble.draw(frame, image)	

