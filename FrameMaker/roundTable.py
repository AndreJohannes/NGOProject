from PIL import Image
from Tools.phrases import Phrases
import Tools.transitions as Transitions

class still:
	
	def __init__(self, start):
		self.startTime = start
		self.stopTime = start + 265
		self.image = Image.open("./images/base15.png")
	
	def draw(self, frame, image):
		if(frame < self.startTime or frame >= self.stopTime):
 			return	
		image.paste(self.image, (0, 0))

class text:
	
	def __init__(self, start, duration, phrase, position, slow=None, color = "black"):
		self.startTime = start
		self.stopTime = start + duration
		self.duration = duration
		self.phrase = phrase 
		self.position = position
		self.slow = slow
		self.color = color

	def draw(self, frame, image):
		if(frame < self.startTime or frame >= self.stopTime):
			return
		idx = frame - self.startTime
		if self.slow == None:
			textMask = self.phrase(idx)
		else:
			textMask = self.phrase(idx if idx < self.slow else (idx - self.slow) / 4 + self.slow)
		image.paste(self.color , self.position, textMask)

class evolve:

	def __init__(self, start):
		self.startTime = start
		self.stopTime = start + 265
		self.list = []
		self.list.append(still(start))
		self.list.append(text(start, 265, Phrases.getPhrase53, (300, 50)))
		self.list.append(text(start + 70, 195, Phrases.getPhrase54, (300, 600), slow=44))
		self.list.append(text(start + 70 + 44, 151, Phrases.getPhrase55, (300+252, 600+50), slow=0, color=(80,147,205)))
		self.list.append(Transitions.blender(None, Image.open("./images/base16.png"), start + 225, 40))

	def draw(self, frame, image):
		if(frame < self.startTime or frame >= self.stopTime):
 			return
 		for obj in self.list:
 			obj.draw(frame, image)
