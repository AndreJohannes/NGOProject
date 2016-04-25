from PIL import Image
from PIL import ImageDraw
import aggdraw
import math
import random
from phrases import Phrases

class RCRectengular:
	@staticmethod
	def draw(d, rec, radius, p):
		d.line((rec[0]+radius,rec[1],rec[2]-radius,rec[1]),p)
		d.line((rec[0]+radius,rec[3],rec[2]-radius,rec[3]),p)
		d.line((rec[0],rec[1]+radius,rec[0],rec[3]-radius),p)
		d.line((rec[2],rec[1]+radius,rec[2],rec[3]-radius),p)
		d.arc((rec[0],rec[1],rec[0]+2*radius,rec[1]+2*radius),90,180,p)
		d.arc((rec[2]-2*radius,rec[1],rec[2],rec[1]+2*radius),0,90,p)
		d.arc((rec[0],rec[3]-2*radius,rec[0]+2*radius,rec[3]),180,270,p)
		d.arc((rec[2]-2*radius,rec[3]-2*radius,rec[2],rec[3]),270,360,p)

class FlipFlop:
	def __init__(self, timeA, timeB):
		self.timeA = timeA
		self.timeB = timeB
		self.onA = False
		self.timerA = 0
		self.timerB = 0

	def inc(self):
		if self.onA:
			self.timerA += 1
			if self.timerA >= self.timeA:
				self.timerB = 0
				self.onA = False
		else:
			self.timerB += 1	
			if self.timerB >= self.timeB:
				self.timerA = 0
				self.onA = True

	def getState(self):
		return self.onA

	def getCount(self):
		return self.timerA

class TimedBubble:
	def __init__(self, pos_x, pos_y, radius, startTime, 
		stopTime, timeA, timeB):
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.radius = radius
		self.timeA = timeA
		self.flipFlop = FlipFlop(timeA, timeB)
		self.counter = 0
		self.startTime = startTime
		self.stopTime = stopTime

	def inc(self):
		self.counter += 1
		if(self.counter>self.startTime):
			self.flipFlop.inc()

	def draw(self,im):
		if self.counter < self.startTime or self.counter > self.stopTime:
			return
		d = aggdraw.Draw(im)
		p = aggdraw.Pen("black", 2.5)
		color = int(255-(255*self.flipFlop.getCount())/self.timeA) 
		p = aggdraw.Pen((color, color, color), 2.5);
		if self.flipFlop.getState():
			d.ellipse((self.pos_x-self.radius, self.pos_y-self.radius, 
				self.pos_x+self.radius,self.pos_y+self.radius), p)
		d.flush()

class MorphingTextBox:
	
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
		y = self.pos_y - (dt)
		x = self.pos_x - self.randomShift*math.sqrt((dt))
		radius = int(max(self.radius - dt / 2.,5))
		hdx = min(int(self.radius + dt / 2.),(self.image.size[0]+radius)/2)
		hdy = min(int(self.radius + dt / 4.),(self.image.size[1]+radius)/2)
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
		self.bubble1 = TimedBubble(pos_x,358,10,startTime,startTime+105,30,5)
		self.bubble2 = TimedBubble(pos_x,318,15,startTime,startTime+105,20,15)
		self.bubble3 = TimedBubble(pos_x,268,20,startTime,startTime+105,10,25)
		self.rectangualar = MorphingTextBox(image, pos_x,268,20,startTime+105)

	def inc(self):
		self.bubble1.inc()
		self.bubble2.inc()
		self.bubble3.inc()
		self.rectangualar.inc()

	def draw(self, im):
		self.bubble1.draw(im)
		self.bubble2.draw(im)
		self.bubble3.draw(im)
		self.rectangualar.draw(im)		

base = Image.open("./base.png")

iOffset = 456
firstThought = OneThought(0, Phrases.getPhrase1(),380)
secondThought = OneThought(80, Phrases.getPhrase3(),945)
thirdThought = OneThought(160, Phrases.getPhrase2(),380)
forthThought = OneThought(240, Phrases.getPhrase4(),945)

for i in range(0,450):
	im = Image.new("RGBA",(1280,720),"white")
	im.paste(base,(0,0))
	firstThought.draw(im)
	secondThought.draw(im)
	thirdThought.draw(im)
	forthThought.draw(im)
	d = ImageDraw.Draw(im)
	d.text((0,0),str(i+iOffset),"black")
	firstThought.inc()
	secondThought.inc()
	thirdThought.inc()
	forthThought.inc()
	print "saving image:" , i 
	#im.save("./images/image" + str(i+iOffset) + ".png","png")
	im.save("../Movie/image" + str(i+iOffset) + ".png","png")

 	