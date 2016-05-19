from PIL import Image
from PIL import ImageDraw
from PIL import ImageOps
import aggdraw
import math
import random
from Tools.phrases import Phrases
from Tools.flags import Flags
import Tools.tools as Tools
import Tools.transitions as Transitions
import Tools.helpers as Helper

class still:
	def __init__(self, start):
		self.startTime = start
		self.stopTime = start + 615
		self.image =  Image.open("./images/base2.png")
	
	def draw(self, frame, image):
		if(frame < self.startTime or frame >= self.stopTime):
 			return	
		image.paste(self.image, (0,0))

class bubble:
	
	def __init__(self, pos_x, pos_y, radius, startTime):
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.radius = radius
		self.startTime = startTime

	def draw(self,frame, im):
		if frame < self.startTime: 
			return 
		idx = frame - self.startTime
		k = min(1,0.2*math.sqrt(idx))
		radius_x = (1-k) * self.radius +k *600
		radius_y = (1-k) * self.radius +k *320
		pos_x = (1-k)*self.pos_x + k * 640
		pos_y = (1-k)*self.pos_y + k * 360	
		canvas = aggdraw.Draw(im)
		pen  = aggdraw.Pen("black", 3)
		brush = aggdraw.Brush((255,255,180),230);
		path = aggdraw.Path()
		for grad in range(0,360):
			dr = 20 * math.pow(math.sin(2*grad/180.*math.pi),2)
			x = (dr+radius_x) * math.sin(grad/180.*math.pi)
			y = (dr+radius_y) * math.cos(grad/180.*math.pi)
			path.lineto(pos_x+x, pos_y+y)

		canvas.polygon(path.coords(),pen, brush)
		canvas.flush()

class OneThought:

	def __init__(self, startTime, pos_x, left):
		self.bubble = Tools.MovingBubble(pos_x,163,10,startTime, 20, left)
		pos_x += -100 if left else 100
		self.rectangualar = bubble( pos_x,139,20,startTime+20)

	def draw(self, frame, image):
		self.bubble.draw(frame, image)
		self.rectangualar.draw(frame, image)

class leaf:

	def __init__(self, startTime, boomTime, pos_y, image):
		self.pos_y = pos_y 
		self.startTime = startTime
		self.boomTime = boomTime
		self.image = image

	def draw(self, frame, image):
		if frame < self.startTime:
			return
		if frame < self.boomTime:
			leaf_rsz = self.image.resize((80,80),Image.ANTIALIAS)
			image.paste("black", (100, self.pos_y), leaf_rsz)	
		elif frame <= self.boomTime + 5:
			idx = frame - self.boomTime
			leaf_rsz2 = self.image.resize((80+50*idx,80+50*idx),Image.ANTIALIAS)
			image.paste(leaf_rsz2, (100-25*idx,self.pos_y-25*idx), leaf_rsz2)
		else:
			leaf_rsz = self.image.resize((80,80),Image.ANTIALIAS)
			image.paste(leaf_rsz, (100, self.pos_y), leaf_rsz)	

class text:
	def __init__(self, start, duration, fading, phrase, position):
		self.startTime = start
		self.stopTime = start + duration + fading
		self.duration = duration
		self.fading = fading
		self.phrase = phrase 
		self.position = position

	def draw(self, frame, image):
		if(frame < self.startTime or frame >= self.stopTime):
 			return
 		idx = frame - self.startTime
 		if idx > self.duration: 
 			color = 255.*(1.-(idx-self.duration)/(self.fading-1.))
			textMask = self.phrase(idx)
			textMask2 = Image.new("L",textMask.size,"black")
			textMask2.paste((color),(0,0),textMask)
			image.paste("black",self.position, textMask2)
 		else:
 			textMask = self.phrase(idx)
			image.paste("black",self.position, textMask)

class leafText:
	def __init__(self, start, fading, phrase, position):
		self.startTime = start
		self.stopTime = start + fading + 5
		self.fading = fading
		self.phrase = phrase 
		self.position = position

	def draw(self, frame, image):
		if(frame < self.startTime or frame >= self.stopTime):
 			return
 		idx = frame - self.startTime
 		if idx <= 5 : 
 			color = int(255/5. * idx)
 		else:
 			color = int(255-255/(self.fading-1.) * (idx-5))
		textMask = self.phrase(1000)
		textMask2 = Image.new("L",textMask.size,"black")
		textMask2.paste((color),(0,0),textMask)
		image.paste("black",self.position, textMask2)

class evolve:

	def __init__(self, start):
		self.startTime = start
		self.stopTime = start + 615
		self.list = []
		self.list.append(still(start))
		self.list.append(OneThought(start, 500, True))
		self.list.append(text(start + 50, 190, 50,  Phrases.getPhrase47, (110,240) ))
		self.list.append(text(start + 290, 90, 50,  Phrases.getPhrase49, (250,280) ))
		self.list.append(leaf(start+430, start+440, 200, Image.open("./images/leaf1.png")))
		self.list.append(leafText(start+445, 50, Phrases.getPhrase50, (300,200) ))
		self.list.append(leaf(start+430, start+490, 300, Image.open("./images/leaf2.png")))
		self.list.append(leafText(start+495, 50, Phrases.getPhrase51, (300,300) ))
		self.list.append(leaf(start+430, start+540, 400, Image.open("./images/leaf3.png")))
		self.list.append(leafText(start+545, 50, Phrases.getPhrase52, (300,400) ))
		self.list.append(Transitions.blender(None, Image.open("./images/base14.png"),start+595, 20))

	def draw(self, frame, image):
		if(frame < self.startTime or frame >= self.stopTime):
 			return
 		for obj in self.list:
 			obj.draw(frame, image)