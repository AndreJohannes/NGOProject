from PIL import Image
from Tools.phrases import Phrases
import Tools.transitions as Transitions


class still:
	def __init__(self, start):
		self.startTime = start
		self.stopTime = start + 200
		self.image = Image.open("./images/base2.png")
	
	def draw(self, frame, image):
		if(frame < self.startTime or frame >= self.stopTime):
			return
		image.paste(self.image, (0, 0))

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
			color = 255.*(1. - (idx - self.duration) / (self.fading - 1.))
			textMask = self.phrase(idx)
			textMask2 = Image.new("L", textMask.size, "black")
			textMask2.paste((color), (0, 0), textMask)
			image.paste("black", (50, int(300 - 1.5 * idx)), textMask2)
		else:
			textMask = self.phrase(idx)
			image.paste("black", (50, int(300 - 1.5 * idx)), textMask)

class evolve:

	def __init__(self, start):
		self.startTime = start
		self.stopTime = start + 200
		self.list = []
		self.list.append(still(start))
		self.list.append(text(start, 150, 50, Phrases.getPhrase55))
		self.list.append(Transitions.zapping(None, Image.open("./images/base15.png"), start + 180, 20))

	def draw(self, frame, image):
		if(frame < self.startTime or frame >= self.stopTime):
			return
		for obj in self.list:
			obj.draw(frame, image)
