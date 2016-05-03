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
		self.bubble1 = Tools.MovingBubble(pos_x,163,10,startTime, None, True)
		self.bubble2 = Tools.MovingBubble(pos_x,163,10,startTime+30, None, True)
		self.bubble3 = Tools.MovingBubble(pos_x,163,10,startTime+60, startTime + 80, True)
		self.rectangualar = Tools.MorphingTextBox(image, 400,139,20,startTime+80, True)

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


thoughts = [OneThought(0, Phrases.getPhrase25(),500)]

production = True
iOffset = 1646 if production else 0

for i in range(0,200):
	im = Image.new("RGBA",(1280,720),"white")
	base = Image.open("./images/rollingeyes/image"+ "{:02d}".format(max(min(i-30,56),0)) +".png")
	if(i>150):
		m = 10 * (i - 150) - 126
		base2 = Image.open("./base3.png")
		mask = Image.new("L",(1280,720),"black")
		d = ImageDraw.Draw(mask)
		for x in range(0,1280):
			for y in range(0,720):
				d.point((x,y),random.randint(max(m-126,0),min(m+126,255)))
		#mask.paste("black",(0,0,dic[i-170],720))
		base.paste(base2,(0,0),mask)
	im.paste(base,(0,0))
	for thought in thoughts:
		thought.draw(im)
		thought.inc()
	d = ImageDraw.Draw(im)
	d.text((0,0),str(i+iOffset),"black")
	print "saving image:" , i 
	im.save("./images/image" + str(i+iOffset) + ".png","png") if not production else im.save("../Movie/images/image" + str(i+iOffset) + ".png","png")

