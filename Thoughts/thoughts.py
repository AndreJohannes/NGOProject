from PIL import Image
from PIL import ImageDraw
import aggdraw
import math
import random
from phrases import Phrases
from flags import Flags
import tools as Tools

class TranscendingBubble:

	def __init__(self, image, pos_x, pos_y, radius, startTime):
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.radius = radius 
		self.startTime = startTime
		self.counter = 0
		self.image = image

	def inc(self):
		self.counter += 1

	def draw(self, im):
		if(self.counter < self.startTime):
			return
		dt = self.counter - self.startTime
		radius = self.radius + 10 * dt
		mask = self.getMask(self.pos_x, self.pos_y, radius)
		im.paste(self.image, (0,0,1280,720), mask)
		d = aggdraw.Draw(im)
		p = aggdraw.Pen("black", 2.5)
		#b = aggdraw.Brush("white")
		radius = self.radius + 10 * dt
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

class OneThought:

	def __init__(self, startTime, image, pos_x):
		self.bubble1 = Tools.TimedBubble(pos_x,358,10,startTime,startTime+35,30,5)
		self.bubble2 = Tools.TimedBubble(pos_x,318,15,startTime,startTime+35,20,15)
		self.bubble3 = Tools.TimedBubble(pos_x,268,20,startTime,startTime+35,10,25)
		self.rectangualar = Tools.MorphingTextBox(image, pos_x,268,20,startTime+35)

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
			color = min(255,(self.counter-self.startTime)*30)
			mask = Image.new("L",self.image.size,(color))
			im.paste(self.image,(self.pos_x,self.pos_y),mask)

	def inc(self):
		self.counter += 1


class ThoughtfulTransition:
	def __init__(self, startTime, image, pos_x):
		self.bubble1 = Tools.TimedBubble(pos_x,358,10,startTime,startTime+35,30,5)
		self.bubble2 = Tools.TimedBubble(pos_x,318,15,startTime,startTime+35,20,15)
		self.bubble3 = Tools.TimedBubble(pos_x,268,20,startTime,startTime+35,10,25)
		self.transcendingBubble = TranscendingBubble(image, pos_x, 268, 20, 
			startTime+35)

	def inc(self):
		self.bubble1.inc()
		self.bubble2.inc()
		self.bubble3.inc()
		self.transcendingBubble.inc()

	def draw(self, im):
		self.bubble1.draw(im)
		self.bubble2.draw(im)
		self.bubble3.draw(im)
		self.transcendingBubble.draw(im)	

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

flags = [OneFlag(190, 260, "germany", 826, 349)]
flags.append(OneFlag(220, 290, "namerica", 462, 349))
flags.append(OneFlag(250, 320, "russia", 826, 349))
flags.append(OneFlag(280, 350, "guatemala", 462, 349))
flags.append(OneFlag(310, 380, "spain", 826, 349))
flags.append(OneFlag(340, 410, "honduras", 462, 349))
flags.append(OneFlag(370, 440, "scottland", 826, 349))
flags.append(OneFlag(400, 470, "brazil", 462, 349))
flags.append(OneFlag(430, 500, "australia", 826, 349))
flags.append(OneFlag(460, 530, "argentina", 462, 349))
flags.append(OneFlag(490, 560, "nigeria", 826, 349))

pensombre = Image.open("./pensombre.png")
thoughts.append(ThoughtfulTransition(650, pensombre, 380))


production = True
iOffset = 456 if production else 0

for i in range(0,800):
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

 	