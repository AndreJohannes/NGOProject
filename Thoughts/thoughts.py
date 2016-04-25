from PIL import Image
from PIL import ImageDraw
import aggdraw
import math
import random
from phrases import Phrases
from flags import Flags

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
		self.bubble1 = TimedBubble(pos_x,358,10,startTime,startTime+35,30,5)
		self.bubble2 = TimedBubble(pos_x,318,15,startTime,startTime+35,20,15)
		self.bubble3 = TimedBubble(pos_x,268,20,startTime,startTime+35,10,25)
		self.rectangualar = MorphingTextBox(image, pos_x,268,20,startTime+35)

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

class OneFlag:

	def __init__(self, startTime, stopTime, name, pos_x, pos_y):
		flags = Flags() 
		self.image = flags.getFlag(name)
		self.startTime = startTime
		self.stopTime = stopTime
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.counter = 0

	def draw(self, im):
		if self.counter>=self.startTime and self.counter<=self.stopTime:
			color = min(255,(self.counter-self.startTime)*50)
			mask = Image.new("L",self.image.size,(color))
			im.paste(self.image,(self.pos_x,self.pos_y),mask)

	def inc(self):
		self.counter += 1


base = Image.open("./base.png")

thoughts = [OneThought(0, Phrases.getPhrase1(),380)]
thoughts.append(OneThought(30, Phrases.getPhrase2(),945))
thoughts.append(OneThought(60, Phrases.getPhrase3(),380))
thoughts.append(OneThought(90, Phrases.getPhrase4(),945))
thoughts.append(OneThought(120, Phrases.getPhrase5(),380))
thoughts.append(OneThought(150, Phrases.getPhrase7(),945))
thoughts.append(OneThought(180, Phrases.getPhrase6(),380))
thoughts.append(OneThought(210, Phrases.getPhrase9(),945))
thoughts.append(OneThought(240, Phrases.getPhrase8(),380))
thoughts.append(OneThought(270, Phrases.getPhrase11(),945))
thoughts.append(OneThought(300, Phrases.getPhrase10(),380))
thoughts.append(OneThought(330, Phrases.getPhrase13(),945))
thoughts.append(OneThought(360, Phrases.getPhrase12(),380))
thoughts.append(OneThought(390, Phrases.getPhrase15(),945))
thoughts.append(OneThought(420, Phrases.getPhrase14(),380))
thoughts.append(OneThought(450, Phrases.getPhrase16(),945))

thoughts.append(OneThought(480, Phrases.getPhrase17(),380))
thoughts.append(OneThought(510, Phrases.getPhrase18(),945))
thoughts.append(OneThought(540, Phrases.getPhrase19(),380))
thoughts.append(OneThought(570, Phrases.getPhrase20(),945))
thoughts.append(OneThought(600, Phrases.getPhrase21(),380))

flags = [OneFlag(190, 255, "germany", 826, 349)]
flags.append(OneFlag(220, 285, "namerica", 462, 349))
flags.append(OneFlag(250, 315, "russia", 826, 349))
flags.append(OneFlag(280, 345, "guatemala", 462, 349))
flags.append(OneFlag(310, 375, "spain", 826, 349))
flags.append(OneFlag(340, 405, "honduras", 462, 349))
flags.append(OneFlag(370, 435, "scottland", 826, 349))
flags.append(OneFlag(400, 465, "brazil", 462, 349))
flags.append(OneFlag(430, 495, "australia", 826, 349))
flags.append(OneFlag(460, 525, "argentina", 462, 349))
flags.append(OneFlag(490, 555, "nigeria", 826, 349))

production = True
iOffset = 456 if production else 0

for i in range(0,700):
	im = Image.new("RGBA",(1280,720),"white")
	im.paste(base,(0,0))
	for thought in thoughts:
		thought.draw(im)
		thought.inc()
	for flag in flags:
		flag.draw(im)
		flag.inc()
	d = ImageDraw.Draw(im)
	d.text((0,0),str(i+iOffset),"black")
	print "saving image:" , i 
	im.save("./images/image" + str(i+iOffset) + ".png","png") if not production else im.save("../Movie/image" + str(i+iOffset) + ".png","png")

 	