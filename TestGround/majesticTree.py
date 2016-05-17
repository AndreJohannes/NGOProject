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
		self.stopTime = start + 100
		self.image =  Image.open("./images/base14.png")
	
	def draw(self, frame, image):
		if(frame < self.startTime or frame >= self.stopTime):
 			return	
		image.paste(self.image, (0,0))

class evolve:

	def __init__(self, start):
		self.startTime = start
		self.stopTime = start + 100
		self.list = []
		self.list.append(still(start))
		self.list.append(Transitions.zapping(None, Image.open("./images/base15.png"),start+80,20))

	def draw(self, frame, image):
		if(frame < self.startTime or frame >= self.stopTime):
 			return
 		for obj in self.list:
 			obj.draw(frame, image)