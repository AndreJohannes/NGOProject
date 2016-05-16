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

class seeding:

	def __init__(self, start):
		self.startTime = start
		self.stopTime = start + 50

	def draw(self, frame, image):
		if(frame < self.startTime or frame >= self.stopTime):
 			return
		idx = frame - self.startTime
 		im = Image.open("../BuildFoundation/images/seeding/image{}.png".format(min(idx, 33))) 
		image.paste(im, (0,46))

class watering:

	def __init__(self, start):
		self.startTime = start
		self.stopTime = start + 50

	def draw(self, frame, image):
		if(frame < self.startTime or frame >= self.stopTime):
 			return
		idx = frame - self.startTime
 		im = Image.open("../BuildFoundation/images/watering/image{:02d}.png".format(min(idx, 41))) 
		image.paste(im, (0,46))

class growing:
	def __init__(self, start):
		self.startTime = start
		self.stopTime = start + 300

	def draw(self, frame, image): 
		if(frame < self.startTime or frame >= self.stopTime):
 			return
		idx = frame - self.startTime
 		im = Image.open("../BuildTree/images/image{}.png".format(min(int(idx-idx*idx/980.), 199))) 
 		if idx > 170:
 			mask = Image.new("L",(1280,720),max(255-(idx-170),165))
			image.paste(im, (0,0),mask)
		else:
			image.paste(im, (0,0))	

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
			image.paste("black",(50, 300-idx),textMask2)
 		else:
 			textMask = self.phrase(idx)
			image.paste("black",(50, 300-idx),textMask)		


class cultivate:

	def __init__(self, start):
		self.startTime = start
		self.stopTime = start + 1350
		self.list = []
		self.list.append(seeding(start))
		self.list.append(watering(start + 50))
		self.list.append(growing(start + 100))
		self.list.append(text(start + 80,70,50,Phrases.getPhrase29))
		self.list.append(text(start + 280,70,50,Phrases.getPhrase30))

	def draw(self, frame, image):
		if(frame < self.startTime or frame >= self.stopTime):
 			return
 		for obj in self.list:
 			obj.draw(frame, image)