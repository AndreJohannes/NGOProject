import aggdraw
from PIL import Image

class title:

	def __init__(self,start, length, position):
		self.startTime = start
		self.stopTime = start + length
		self.title = Image.open("./images/title.png")
		self.position = position

	def draw(self, frame, image):
		if(frame < self.startTime or frame >= self.stopTime):
 			return
 		idx = frame - self.startTime
 		if idx < 70:
 			color = min(5*(idx),255)
 		else: 
 			color = max(255-5*(idx-70),0)
 		mask = Image.new("L", self.title.size, color)
		image.paste(self.title, self.position, mask)	
