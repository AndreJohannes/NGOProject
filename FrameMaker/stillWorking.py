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

class labour:

	def __init__(self, start):
		self.startTime = start
		self.stopTime = start + 100

	def draw(self, frame, image):
		if(frame < self.startTime or frame >= self.stopTime):
 			return
		idx = frame - self.startTime
 		im = Image.open("../WorkOnFoundation/images/image{}.png".format(idx))
		image.paste(im, (0, 0))

class slider:

	def __init__(self, start):
		self.startTime = start
		self.stopTime = start + 100

	def draw(self, frame, image):
		if(frame < self.startTime or frame >= self.stopTime):
 			return
		idx = frame - self.startTime
		base = Image.open("../WorkOnFoundation/images/image{}.png".format(idx + 100))
 		im = Image.open("../Pensombre/images/slider/image{:02d}.png".format(25 - idx)).convert("RGBA")
 		dic = {10:1221, 11:1196, 12:1153, 13:1096, 14:1022, 15:952, 16:874, 17:797, 18:724, 19:646, 20:562, 21:476, 22:391, 23:297, 24:208, 25:80}
		if(dic.has_key(25 - idx)):
			mask = Image.new("L", (1280, 720), "white")
			mask.paste("black", (0, 0, dic[25 - idx], 720))
			im.paste(base, (0, 0), mask)
		image.paste(im, (0, 0))

class text:

	def __init__(self, start):
		self.startTime = start
		self.stopTime = start + 125

	def draw(self, frame, image):	
		if(frame < self.startTime or frame >= self.stopTime):
 			return
		idx = frame - self.startTime
		if idx > 100: 
 			color = 255.*(1. - (idx - 100) / (25.))
			textMask = Phrases.getPhrase46(idx)
			textMask2 = Image.new("L", textMask.size, "black")
			textMask2.paste((color), (0, 0), textMask)
			image.paste("black", (65, 300 - idx), textMask2)
 		else:
			textMask = Phrases.getPhrase46(idx)
			image.paste("black", (65, 300 - idx), textMask)

class evolve:

	def __init__(self, start):
		self.startTime = start
		self.stopTime = start + 125
		self.list = []
		self.list.append(labour(start))
		self.list.append(slider(start + 100))
		self.list.append(text(start))

	def draw(self, frame, image):
		if(frame < self.startTime or frame >= self.stopTime):
 			return
 		for obj in self.list:
 			obj.draw(frame, image)
