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

class growing:

	def __init__(self, start):
		self.startTime = start
		self.stopTime = start + 120

	def draw(self, frame, image):
		if(frame < self.startTime or frame >= self.stopTime):
 			return
		idx = frame - self.startTime
 		im = Image.open("../LeaveGrowing/images/preps/image{}.png".format(min(idx+100,199))) 
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
			image.paste("black",(50, 300-0*idx),textMask2)
 		else:
 			textMask = self.phrase(idx)
			image.paste("black",(50, 300-0*idx),textMask)

class textOnLeaf:
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
 		if idx < self.duration: 
 			color = 255.*(0.+(idx)/(self.duration-1.))
			textMask = self.phrase(idx)
			textMask2 = Image.new("L",textMask.size,"black")
			textMask2.paste((color),(0,0),textMask)
			image.paste("white", self.position, textMask2)
 		else:
 			textMask = self.phrase(idx)
			image.paste("white", self.position, textMask)

class flash:
	def __init__(self, start, position):
		self.startTime = start
		self.stopTime = start + 10
		self.position = position
		self.image =  Image.open("./images/flash.png")
	
	def draw(self, frame, image):
		if(frame < self.startTime or frame >= self.stopTime):
 			return
 		idx = frame - self.startTime
 		sz = (idx+1) * 100
 		flash_rsz = self.image.resize((sz,sz),Image.ANTIALIAS)
		image.paste((255,255,180),(self.position[0]-sz/2,self.position[1]-sz/2),flash_rsz)


class evolve:

	def __init__(self, start):
		self.startTime = start
		self.stopTime = start + 140
		self.list = []
		self.list.append(growing(start))
		self.list.append(text(start,70,50,Phrases.getPhrase31))
		self.list.append(textOnLeaf(start + 30,35,55,Phrases.getPhrase34, (737, 426)))
		self.list.append(textOnLeaf(start + 40,30,50,Phrases.getPhrase35, (438, 462)))
		self.list.append(textOnLeaf(start + 20,30,70,Phrases.getPhrase33, (491, 123)))
		self.list.append(textOnLeaf(start + 30,70,20,Phrases.getPhrase32, (170, 400)))
		self.list.append(flash(start + 49,(603,157)))
		self.list.append(flash(start + 65,(793,454)))
		self.list.append(flash(start + 83,(495,492)))
		self.list.append(flash(start + 100,(295,477)))
		self.list.append(Transitions.pageFlip( Image.open("./images/base9.png"), Image.open("./images/base10.png").convert("RGBA"),start+120,20))

	def draw(self, frame, image):
		if(frame < self.startTime or frame >= self.stopTime):
 			return
 		for obj in self.list:
 			obj.draw(frame, image)

