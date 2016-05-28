from PIL import Image
from Tools.phrases import Phrases
import Tools.transitions as Transitions
import aggdraw
import math

class still:
	
	def __init__(self, start):
		self.startTime = start
		self.stopTime = start + 230
		self.image = Image.open("./images/base2.png")
	
	def draw(self, frame, image):
		if(frame < self.startTime or frame >= self.stopTime):
			return
		image.paste(self.image, (0, 0))

class bubble:
	
	def __init__(self, startTime):
		self.startTime = startTime

	def draw(self, frame, im):
		if frame < self.startTime: 
			return 
		# idx = frame - self.startTime
		radius_x = 600
		radius_y = 320
		pos_x = 640
		pos_y = 360	
		canvas = aggdraw.Draw(im)
		pen = aggdraw.Pen("black", 3)
		brush = aggdraw.Brush((255, 255, 180), 230);
		path = aggdraw.Path()
		for grad in range(0, 360):
			dr = 20 * math.pow(math.sin(2 * grad / 180.*math.pi), 2)
			x = (dr + radius_x) * math.sin(grad / 180.*math.pi)
			y = (dr + radius_y) * math.cos(grad / 180.*math.pi)
			path.lineto(pos_x + x, pos_y + y)

		canvas.polygon(path.coords(), pen, brush)
		canvas.flush()

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
			image.paste("black", (620 - textMask2.size[0] / 2, int(165 - 0 * idx)), textMask2)
		else:
			textMask = self.phrase(idx)
			image.paste("black", (620 - textMask.size[0] / 2, int(165 - 0 * idx)), textMask)
			
class smile:
	
	def __init__(self):
		pass
	
	def draw(self, frame, image):
		im = Image.open("./emoticon/smile.png")
		image.paste("white", (620, 435, 810, 473))
		image.paste(im, (0, 0), im)	
		

class evolve:

	def __init__(self, start):
		self.startTime = start
		self.stopTime = start + 230
		self.list = []
		self.list.append(still(start))
		self.list.append(smile())
		self.list.append(bubble(start))
		font1 = aggdraw.Font("white", "./fonts/calibri.ttf", 46)
		phrase1 = ["Join us in breaking down walls.",
			"             ",
			"Support these three initiatives.",
			"             ",
			"Help us grow our tree.",
			"             ",
			"Global citizens thrive in informed collaboration!"]
		self.list.append(text(start, 180, 50, Phrases().makeImage_centered_runnable(phrase1, font1)))
		self.list.append(Transitions.zapping(None, Image.open("./images/base15.png"), start + 180, 20))

	def draw(self, frame, image):
		if(frame < self.startTime or frame >= self.stopTime):
			return
		for obj in self.list:
			obj.draw(frame, image)
