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
import Tools.helpers as Helpers

class image:

	def __init__(self, start, duration, image):
		self.startTime = start
		self.stopTime = start + duration
		self.duration = duration
		self.image = image

	def draw(self, frame, image):
		if(frame < self.startTime or frame >= self.stopTime):
 			return
 		image.paste(self.image, (0,0))

class text:
	def __init__(self, start, duration, fading, phrase):
		self.startTime = start
		self.stopTime = start + duration + fading
		self.duration = duration
		self.fading = fading
		self.phrase = phrase 

	def draw(self, frame, image):
		if(frame < self.startTime or frame >= self.stopTime):
 			return
 		idx = frame - self.startTime
 		if idx > self.duration: 
 			color = 255.*(1.-(idx-self.duration)/(self.fading-1.))
			textMask = self.phrase(idx)
			textMask2 = Image.new("L",textMask.size,"black")
			textMask2.paste((color),(0,0),textMask)
			image.paste("black",(50, int(300-1.5*idx)),textMask2)
 		else:
 			textMask = self.phrase(idx)
			image.paste("black",(50, int(300-1.5*idx)),textMask)

class pullWall:

	def __init__(self, start):
		self.startTime = start
		self.stopTime = start + 360

	def draw(self, frame, image):
		if(frame < self.startTime or frame >= self.stopTime):
 			return
		idx = frame - self.startTime
 		im = Image.open("../BuildFoundation/images/pullWall/image{:03d}.png".format(max(0,min(135,int((idx-120)/2.)))))
		d = aggdraw.Draw(im)
		p = aggdraw.Pen("black", 8.46666)
		d.ellipse((640-315,596,640+315,596),p)
		d.flush()
		im = im.convert("L")
		im = ImageOps.invert(im)
		color = max(190-5*max(0,idx-120),0)
		image.paste((color,color,color),(0,0),im)

class handShake:

	def __init__(self, start):
		self.startTime = start
		self.stopTime = start + 320

	def draw(self, frame, image):
		if(frame < self.startTime or frame >= self.stopTime):
 			return
		idx = frame - self.startTime
 		im = Image.open("../BuildFoundation/images/handshake/image{:02d}.png".format(min(int((idx)/2), 15))) 
		d = aggdraw.Draw(im)
		p = aggdraw.Pen("black", 8.46666)
		d.ellipse((640-315,596,640+315,596),p)
		d.flush()
		im = im.convert("L")
		im = ImageOps.invert(im)
		color = min(5*idx,190)
		image.paste((color,color,color),(0,0),im)

class evolve:

	def __init__(self, start):
		self.startTime = start
		self.stopTime = start + 1170
		self.list = []
		self.list.append(image(start, 470, Helpers.open_image("./images/base4.png",190)))
		self.list.append(text(start, 420, 50, Phrases.getPhrase26))
		self.list.append(pullWall(start + 470))
		self.list.append(text(start + 470, 310, 50, Phrases.getPhrase27))
		self.list.append(handShake(start + 830))
		self.list.append(text(start + 830, 270, 50, Phrases.getPhrase28))
		self.list.append(Transitions.horizontalFlip(Helpers.open_image("./images/base5.png",190).convert("RGBA"),Image.open("./images/base6.png").convert("RGBA"),start+1150,20))

	def draw(self, frame, image):
		if(frame < self.startTime or frame >= self.stopTime):
 			return
 		for obj in self.list:
 			obj.draw(frame, image)