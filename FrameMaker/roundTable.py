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
		self.stopTime = start + 150
		self.image =  Image.open("./images/base15.png")
	
	def draw(self, frame, image):
		if(frame < self.startTime or frame >= self.stopTime):
 			return	
		image.paste(self.image, (0,0))

class text:
	def __init__(self, start, duration, phrase, position):
		self.startTime = start
		self.stopTime = start + duration
		self.duration = duration
		self.phrase = phrase 
		self.position = position

	def draw(self, frame, image):
		if(frame < self.startTime or frame >= self.stopTime):
 			return
 		idx = frame - self.startTime
 		textMask = self.phrase(idx)
		image.paste("black", self.position, textMask)

class evolve:

	def __init__(self, start):
		self.startTime = start
		self.stopTime = start + 150
		self.list = []
		self.list.append(still(start))
		self.list.append(text(start,150,Phrases.getPhrase53,(300,50)))
		self.list.append(text(start+70,80,Phrases.getPhrase54,(300,600)))

	def draw(self, frame, image):
		if(frame < self.startTime or frame >= self.stopTime):
 			return
 		for obj in self.list:
 			obj.draw(frame, image)