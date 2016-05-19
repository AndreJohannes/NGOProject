import aggdraw
from PIL import Image
import math

class wall:

	def __init__(self,start):
		self.startTime = start
		self.stopTime = start + 35

	def draw(self, frame, image):
		if(frame < self.startTime or frame >= self.stopTime):
 			return
 		idx = (frame - self.startTime)/2
		im = Image.open("../WallBuilding/images/wall"+ "{:02d}".format(idx) +".png")
		im = im.convert("RGBA");
		image.paste(im,(0,0),im)
		d = aggdraw.Draw(image)
		p = aggdraw.Pen("black", 8.46666)
		d.ellipse((640-315,596,640+315,596),p)
		d.flush()
