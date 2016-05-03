from PIL import Image
from PIL import ImageDraw
import aggdraw
import math
import random
from Python.phrases import Phrases
from Python.flags import Flags
import Python.tools as Tools



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


class ThoughtfulTransition:
	def __init__(self, startTime, image, pos_x):
		self.bubble1 = Tools.TimedBubble(pos_x,358,10,startTime,startTime+35,30,5)
		self.bubble2 = Tools.TimedBubble(pos_x,318,15,startTime,startTime+35,20,15)
		self.bubble3 = Tools.TimedBubble(pos_x,268,20,startTime,startTime+35,10,25)
		self.transcendingBubble = Tools.TranscendingBubble(image, pos_x, 268, 20, 
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
d = aggdraw.Draw(base)
p = aggdraw.Pen("black", 8.46666)
d.ellipse((640-315,596,640+315,596),p)
d.flush()

thoughts = [OneThought(0, Phrases.getPhrase23(),380)]
thoughts.append(OneThought(30, Phrases.getPhrase24(),945))

pensombre = Image.open("./pensombre.png")
thoughts.append(ThoughtfulTransition(80, pensombre, 945))


production = True
iOffset = 1436 if production else 0

for i in range(0,210):
	im = Image.new("RGBA",(1280,720),"white")
	im.paste(base,(0,0))
	for thought in thoughts:
		thought.draw(im)
		thought.inc()
	d = ImageDraw.Draw(im)
	d.text((0,0),str(i+iOffset),"black")
	print "saving image:" , i 
	im.save("./images/image" + str(i+iOffset) + ".png","png") if not production else im.save("../Movie/images/image" + str(i+iOffset) + ".png","png")

 	