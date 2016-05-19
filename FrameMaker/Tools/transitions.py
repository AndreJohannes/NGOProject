from PIL import Image
from PIL import ImageDraw
import aggdraw
import math
import random
import Tools.helpers as helpers

class blender:
	
	def __init__(self, image1, image2, start, duration):
		self.image1 = image1
		self.image2 = image2
		self.startTime = start
		self.duration = duration
		self.stopTime = start + duration

	def draw(self, frame, image):
		if frame < self.startTime or frame >= self.stopTime:
			return
		idx = frame - self.startTime
		color = (255. * idx) / (self.duration)	
		if self.image1 != None:
			image.paste(self.image1, (0,0))
		mask = Image.new("L",(1280,720),(color))
		image.paste(self.image2, (0,0), mask)

class zapping:
	
	def __init__(self, image1, image2, start, duration):
		self.image1 = image1
		self.image2 = image2
		self.startTime = start
		self.duration = duration
		self.stopTime = start + duration

	def draw(self, frame, image):
		if frame < self.startTime or frame >= self.stopTime:
			return
		idx = frame - self.startTime
		m = int(512 * idx / (1.*self.duration)  - 126)	
		if self.image1 != None:
			image.paste(self.image1, (0,0))
		mask = Image.new("L",(1280,720),"black")
		d = ImageDraw.Draw(mask)
		for x in range(0,1280):
			for y in range(0,720): 
				d.point((x,y),random.randint(min(max(m-126,0),255),min(m+126,255)))
		image.paste(self.image2, (0,0), mask)		


class horizontalFlip:
	
	def __init__(self, image1, image2, start, duration):
		self.image1 = image1
		self.image2 = image2
		self.startTime = start
		self.duration = duration
		self.stopTime = start + duration

	def draw(self, frame, image):
		if frame < self.startTime or frame >= self.stopTime:
			return
		idx = frame - self.startTime
		rect = [[0,420],[1280,420],[1280,720],[0,720]]

		rad = -idx / (1.0*self.duration) * math.pi if idx <= self.duration/2 else -(self.duration-idx) / (1.0*self.duration) * math.pi
 		dz  = 300 * math.sin(rad)
 		C = 2000
		dx1 = 640  * C / (C-dz)
		dy1 = 300 * math.cos(rad) * C / (C-dz) 
		dx2 = 640  * C / (C+dz)
		dy2 = 300 * math.cos(rad) * C / (C+dz) 

		if idx <= self.duration/2:
			pa = [[640-dx1, 420],[640+dx1,420],[640+dx2,420+dy2],[640-dx2,420+dy2]]
			data =  helpers.find_coeffs(pa,rect).tolist()
			tm = self.image1.transform((1280,720), Image.PERSPECTIVE, data,  Image.BICUBIC)
			image.paste(tm,(0,0), tm)
		else:
			pa = [[640-dx2, 420],[640+dx2,420],[640+dx1,420+dy1],[640-dx1,420+dy1]]
			data =  helpers.find_coeffs(pa,rect).tolist()
			tm2 = self.image2.transform((1280,720), Image.PERSPECTIVE,data,  Image.BICUBIC)
			image.paste(tm2,(0,0), tm2)

class pageFlip:

	def __init__(self, image1, image2, start, duration, reverse = False):
		self.image1 = image1
		self.image2 = image2
		self.startTime = start
		self.duration = duration
		self.stopTime = start + duration
		self.reverse = reverse

	def draw(self, frame, image):
		if frame < self.startTime or frame >= self.stopTime:
			return
		idx = frame - self.startTime if self.reverse == False else self.stopTime - 1 - frame
		rect_right = [[640,0],[1280,0],[1280,720],[640,720]]
		rect_left = [[0,0],[640,0],[640,720],[0,720]]

		rad = -idx / (1.0*self.duration) * math.pi if idx <= self.duration/2 else -(self.duration-idx) / (1.0*self.duration) * math.pi

 		dz  = 640 * math.sin(rad)
 		C = 2000
		dx = 640 * math.cos(rad) * C / (C+dz)
		dy = 360 * C / (C+dz) 

		if idx <= self.duration/2:
			pa = [[640, 0],[640+dx,360-dy],[640+dx,360+dy],[640,720]]
			data =  helpers.find_coeffs(pa,rect_right).tolist()
			tm = self.image1.transform((1280,720), Image.PERSPECTIVE,data,  Image.BICUBIC).crop((640,0,1280,720))
			image.paste(self.image1.crop((0,0,640,720)),(0,0))
 			image.paste(self.image2.crop((640,0,1280,720)),(640,0))
			image.paste(tm,(640,0), tm)
		else:
			pa = [[640-dx,360-dy],[640,0],[640,720],[640-dx,360+dy]]
			data =  helpers.find_coeffs(pa,rect_left).tolist()
			tm = self.image2.transform((1280,720), Image.PERSPECTIVE,data,  Image.BICUBIC).crop((0,0,640,720))
			image.paste(self.image1.crop((0,0,640,720)),(0,0))
 			image.paste(self.image2.crop((640,0,1280,720)),(640,0))
			image.paste(tm,(0,0), tm)





