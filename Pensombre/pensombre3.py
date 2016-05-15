from PIL import Image
from PIL import ImageDraw
import aggdraw
import math
import random
from Python.phrases import Phrases
from Python.flags import Flags
import Python.tools as Tools
import Python.transitions as Transitions



class OneThought:

	def __init__(self, startTime, image, pos_x, left):
		self.bubble1 = Tools.MovingBubble(pos_x,163,10,startTime, startTime+20, left)
		##self.bubble2 = Tools.MovingBubble(pos_x,163,10,startTime+30, None, left)
		##self.bubble3 = Tools.MovingBubble(pos_x,163,10,startTime+60, startTime + 80, left)
		pos_x += -100 if left else 100
		self.rectangualar = Tools.MorphingTextBox(image, pos_x,139,20,startTime+20, True)

	def inc(self):
		self.bubble1.inc()
		##self.bubble2.inc()
		##self.bubble3.inc()
		self.rectangualar.inc()

	def draw(self, im):
		self.bubble1.draw(im)
		##self.bubble2.draw(im)
		##self.bubble3.draw(im)
		self.rectangualar.draw(im)	


thoughts = [OneThought(0, Phrases.getPhrase21(),500, True)]
thoughts.append(OneThought(60, Phrases.getPhrase22a(),877, False))
thoughts.append(OneThought(120, Phrases.getPhrase22b(),500, True))
thoughts.append(OneThought(180, Phrases.getPhrase23(),877, False))

production =  True
iOffset = 1310 if production else 0

dOffset = 280
for i in range(0,dOffset):
	im = Image.new("RGBA",(1280,720),"white")
	if(i<=69):
		base = Image.open("./images/pensativo/image{}.png".format(max(min(i-0,39),0)))
	else:
		base = Image.open("base.png");
	im.paste(base,(0,0))
	for thought in thoughts:
		thought.draw(im)
		thought.inc()
	d = ImageDraw.Draw(im)
	d.text((0,0),str(i+iOffset),"black")
	print "saving image:" , i 
	im.save("./images/image" + str(i+iOffset) + ".png","png") if not production else im.save("../Movie/images/image" + str(i+iOffset) + ".png","png")

iOffset += dOffset

def callback(im, i):
	d = ImageDraw.Draw(im)
	d.text((0,0),str(i+iOffset),"black")
	print "saving image:" , i + dOffset
	im.save("./images/image" + str(i+iOffset) + ".png","png") if not production else im.save("../Movie/images/image" + str(i+iOffset) + ".png","png")
Transitions.zapping(im, Image.open("./base4.png").convert("RGBA"), 50, callback)