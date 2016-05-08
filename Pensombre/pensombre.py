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
		self.bubble1 = Tools.MovingBubble(pos_x,163,10,startTime, None)
		self.bubble2 = Tools.MovingBubble(pos_x,163,10,startTime+30, None)
		self.bubble3 = Tools.MovingBubble(pos_x,163,10,startTime+60, startTime + 80)
		self.rectangualar = Tools.MorphingTextBox(image, 977,139,20,startTime+80, True)

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


thoughts = [OneThought(0, Phrases.getPhrase17(), 877)]

dic =  {10:1221,11:1196,12:1153,13:1096,14:1022,15:952,16:874,17:797,18:724,19:646,20:562,21:476,22:391,23:297,24:208,25:80}

production = True
iOffset = 1060 if production else 0

for i in range(0,200):
	im = Image.new("RGBA",(1280,720),"white")
	if(i<=85):
		base = Image.open("./images/rollingeyes/left_right/image{}.png".format(max(min(i-0,47),0)))
	else:
		base = Image.open("./images/rollingeyes/topright/image{}.png".format(max(min(i-85,9),0)))
	if(i>170):
		base = Image.open("./images/slider/image"+ "{:02d}".format(max(min(i-170,28),0)) +".png")
		if(dic.has_key(i-170)):
			base2 = Image.open("./base2.png")
			d = aggdraw.Draw(base2)
			p = aggdraw.Pen("black", 8.46666)
			d.ellipse((640-315,596,640+315,596),p)
			d.flush()
			mask = Image.new("L",(1280,720),"white")
			mask.paste("black",(0,0,dic[i-170],720))
			base.paste(base2,(0,0),mask)
	im.paste(base,(0,0))
	for thought in thoughts:
		thought.draw(im)
		thought.inc()
	d = ImageDraw.Draw(im)
	d.text((0,0),str(i+iOffset),"black")
	print "saving image:" , i + iOffset
	im.save("./images/image" + str(i+iOffset) + ".png","png") if not production else im.save("../Movie/images/image" + str(i+iOffset) + ".png","png")


