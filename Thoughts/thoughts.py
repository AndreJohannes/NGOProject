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

thoughts = [OneThought(0, Phrases.getPhrase2(),380)]
thoughts.append(OneThought(30, Phrases.getPhrase3(),945))
thoughts.append(OneThought(60, Phrases.getPhrase4(),380))
thoughts.append(OneThought(90, Phrases.getPhrase5(),945))
thoughts.append(OneThought(120, Phrases.getPhrase6(),380))
thoughts.append(OneThought(150, Phrases.getPhrase7(),945))
thoughts.append(OneThought(180, Phrases.getPhrase8(),380))
thoughts.append(OneThought(210, Phrases.getPhrase9(),945))
thoughts.append(OneThought(240, Phrases.getPhrase10(),380))
thoughts.append(OneThought(270, Phrases.getPhrase11(),945))
thoughts.append(OneThought(300, Phrases.getPhrase12(),380))
thoughts.append(OneThought(330, Phrases.getPhrase13(),945))
thoughts.append(OneThought(360, Phrases.getPhrase14(),380))
thoughts.append(OneThought(390, Phrases.getPhrase15(),945))
thoughts.append(OneThought(420, Phrases.getPhrase16(),380))

flags = [OneFlag(160, 230, "america", 462, 349)]
flags.append(OneFlag(190, 260, "mexican", 826, 349))
flags.append(OneFlag(220, 290, "argentina", 462, 349))
flags.append(OneFlag(250, 320, "british", 826, 349))
flags.append(OneFlag(280, 350, "germany", 462, 349))
flags.append(OneFlag(310, 380, "spain", 826, 349))
flags.append(OneFlag(340, 410, "japanese", 462, 349))
flags.append(OneFlag(370, 440, "kiwi", 826, 349))

pensombre = Image.open("./pensombre.png")
thoughts.append(ThoughtfulTransition(470, pensombre, 380))


production =  not False
iOffset = 456 if production else 0

for i in range(0,620):
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
	print "saving image:" , i + iOffset
	im.save("./images/image" + str(i+iOffset) + ".png","png") if not production else im.save("../Movie/images/image" + str(i+iOffset) + ".png","png")

 	