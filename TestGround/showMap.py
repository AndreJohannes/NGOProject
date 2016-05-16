from PIL import Image
from PIL import ImageDraw
import aggdraw
import math
import random
from Tools.phrases import Phrases
from Tools.flags import Flags
import Tools.tools as Tools
import Tools.transitions as Transitions
import Tools.helpers as Helpers

class zoom:

	def __init__(self,start):
		self.startTime = start
		self.stopTime = start + 240

	def draw(self, frame, image):
		if(frame < self.startTime or frame >= self.stopTime):
 			return
 		idx = frame - self.startTime
 		image.paste(Image.open("../ZoomInMap/images/preps/image{}.png".format(min(idx, 169))),(0,0))
		if idx >= 170:
			color = 255.*(1-(idx-170)/69.)
			textMask = Phrases.getPhrase24(idx)
			textMask2 = Image.new("L",textMask.size,"black")
			textMask2.paste((color),(0,0),textMask)
			image.paste("black",(50, 280),textMask2)
		else:
			textMask = Phrases.getPhrase24(idx)		
			image.paste("black",(50, 280),textMask)

class zoom2:
	def __init__(self,start):
		self.startTime = start
		self.stopTime = start + 70

	def draw(self, frame, image):
		if(frame < self.startTime or frame >= self.stopTime):
 			return
 		idx = frame - self.startTime
 		image.paste(Image.open("../ZoomInMap/images/preps/image{}.png".format(min(idx+390, 459))),(0,0))

class regions:
	def __init__(self,start):
		self.startTime = start
		self.stopTime = start + 150
		self.blenders = []
		hidalgo = Image.open("./images/hidalgo.png")
		mezquital = Image.open("./images/mezquital.png")
		huasteca = Image.open("./images/huasteca.png")
		otomi = Image.open("./images/otomi.png")
		self.blenders.append(Transitions.blender(hidalgo, mezquital ,start, 50)) 
		self.blenders.append(Transitions.blender(mezquital, huasteca ,start + 50, 50))
		self.blenders.append(Transitions.blender(huasteca, otomi ,start + 100, 50))

	def draw(self, frame, image):
		if(frame < self.startTime or frame >= self.stopTime):
 			return
 		for blender in self.blenders:
 			blender.draw(frame, image)

class areas:
 	def __init__(self, start):
 		self.startTime = start
 		self.stopTime = start + 160
 		self.blenders = []
 		otomi = Image.open("./images/otomi_close.png")
		acaxochitlan = Image.open("./images/acaxochitlan.png")
		tenango = Image.open("./images/tenango.png")
		bartolo = Image.open("./images/bartolo.png")
		huehuetla = Image.open("./images/huehuetla.png")
		self.blenders.append(Transitions.blender(otomi, acaxochitlan, start, 40)) 
		self.blenders.append(Transitions.blender(acaxochitlan, tenango, start + 40, 40))
		self.blenders.append(Transitions.blender(tenango, bartolo, start + 80, 40))
		self.blenders.append(Transitions.blender(bartolo, huehuetla,start + 120, 40))

	def draw(self, frame, image):
		if(frame < self.startTime or frame >= self.stopTime):
 			return
 		for blender in self.blenders:
 			blender.draw(frame, image)

class text2:
	def __init__(self,start):
		self.startTime = start
		self.stopTime = start + 90

	def draw(self, frame, image):
		if(frame < self.startTime or frame >= self.stopTime):
 			return
 		idx = frame - self.startTime
		if idx >= 70:
			color = 255.*(1-(idx-70)/20.)
			textMask = Phrases.getPhrase25(idx)
			textMask2 = Image.new("L",textMask.size,"black")
			textMask2.paste((color),(0,0),textMask)
			image.paste("black",(50, 280),textMask2)
		else:
			textMask = Phrases.getPhrase25(idx)		
			image.paste("black",(50, 280),textMask)


class journey:
	def __init__(self,start):
		self.startTime = start
		self.stopTime = start + 660
		self.zoom = zoom(start)
		self.regions = regions(start + 240)
		self.zoom2 = zoom2(start + 390)
		self.areas = areas(start + 460)
		self.textOverlap2 = text2(start + 390)
		self.transition = Transitions.blender(Image.open("./images/huehuetla.png"), Helpers.open_image("./images/base4.png",190), start + 620, 40)

	def draw(self, frame, image):
		if(frame < self.startTime or frame >= self.stopTime):
 			return
 		self.zoom.draw(frame, image)
 		self.regions.draw(frame, image)	
 		self.zoom2.draw(frame, image)
 		self.areas.draw(frame, image)
 		self.textOverlap2.draw(frame, image)
 		self.transition.draw(frame, image)