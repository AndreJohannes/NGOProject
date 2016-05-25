from PIL import Image
import aggdraw
import math
from Tools.phrases import Phrases
import Tools.tools as Tools
import Tools.transitions as Transitions

class still:
	
	def __init__(self, start):
		self.startTime = start
		self.stopTime = start + 230
		self.image = Image.open("./images/base2.png")
	
	def draw(self, frame, image):
		if(frame < self.startTime or frame >= self.stopTime):
			return	
		image.paste(self.image, (0, 0))

class emoticon:
	
	def __init__(self, start):
		self.startTime = start
		self.stopTime = start + 200
		self.eye_base = Image.new("RGBA", (55, 63), "white")	
		self.eye_left = Image.open("./emoticon/eye_left.png")
		self.eye_right = Image.open("./emoticon/eye_right.png")
	
	def draw(self, frame, image):
		if(frame < self.startTime or frame >= self.stopTime):
			return
		idx = frame - self.startTime		
		im = Image.open("./emoticon/frames/frame{}.png".format(min(int(idx / 2) * 2, 24)))
		image.paste(im, (0, 0))
		self.draw_eye(idx, image)
		self.draw_smile(idx, image)

	def draw_eye(self, idx, image):
		eye_base = self.eye_base.copy()
		# center = (17, 35)
		canvas = aggdraw.Draw(eye_base)
		pen = aggdraw.Pen("black", 0)
		brush = aggdraw.Brush("black", 255)
		if idx > 70:
			canvas.ellipse((55 / 2. - 12, 63 / 2. - 12, 55 / 2. + 12, 63 / 2. + 12), pen, brush)
		else:
			canvas.ellipse((17 - 12, 35 - 12, 17 + 12, 35 + 12), pen, brush)
		pen = aggdraw.Pen("black", 1)
		brush = aggdraw.Brush((248, 249, 118), 255)
		if idx > 70:
			lev = 44 * math.sin(max(0, 5 - (idx - 70)) / 3.)
		else:
			lev = 44 * math.sin(min(5, max(idx - 50, 0)) / 3.)
		canvas.ellipse((27.5 - 100, -90 + lev - 100, 27.5 + 100, -90 + lev + 100), pen, brush)

		canvas.flush()
		eye_left = eye_base.copy()
		eye_left.paste(self.eye_left, (0, 0), self.eye_left)
		eye_right = eye_base
		eye_right.paste(self.eye_right, (0, 0), self.eye_right)
		image.paste(eye_left, (747, 258))
		image.paste(eye_right, (607, 256))

	def draw_smile(self, idx, image):
		if idx <= 70:
			return
		im = Image.open("./emoticon/smile.png")
		image.paste(im, (0, 0), im)	

class animation3D:

	def __init__(self, start):
		self.startTime = start
		self.stopTime = start + 275
	
	def draw(self, frame, image):
		if(frame < self.startTime or frame >= self.stopTime):
			return
		idx = frame - self.startTime		
		im = Image.open("./animation3D/frames/frame{}.png".format(min(idx, 200)))	
		image.paste(im, (0, 0))

class bubble:
	
	def __init__(self, pos_x, pos_y, radius, startTime):
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.radius = radius
		self.startTime = startTime

	def draw(self, frame, im):
		if frame < self.startTime: 
			return 
		idx = frame - self.startTime
		k = min(1, 0.2 * math.sqrt(idx))
		radius_x = (1 - k) * self.radius + k * 600
		radius_y = (1 - k) * self.radius + k * 320
		pos_x = (1 - k) * self.pos_x + k * 640
		pos_y = (1 - k) * self.pos_y + k * 360	
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

class OneThought:

	def __init__(self, startTime, pos_x, left):
		self.bubble = Tools.MovingBubble(pos_x, 163, 10, startTime, 20, left)
		pos_x += -100 if left else 100
		self.rectangualar = bubble(pos_x, 139, 20, startTime + 20)

	def draw(self, frame, image):
		self.bubble.draw(frame, image)
		self.rectangualar.draw(frame, image)

class leaf:

	def __init__(self, startTime, boomTime, pos_y, image):
		self.pos_y = pos_y 
		self.startTime = startTime
		self.boomTime = boomTime
		self.image = image

	def draw(self, frame, image):
		if frame < self.startTime:
			return
		if frame < self.boomTime:
			leaf_rsz = self.image.resize((80, 80), Image.ANTIALIAS)
			image.paste("black", (150, self.pos_y), leaf_rsz)	
		elif frame <= self.boomTime + 5:
			idx = frame - self.boomTime
			leaf_rsz2 = self.image.resize((80 + 50 * idx, 80 + 50 * idx), Image.ANTIALIAS)
			image.paste(leaf_rsz2, (150 - 25 * idx, self.pos_y - 25 * idx), leaf_rsz2)
		else:
			leaf_rsz = self.image.resize((80 + 50, 80 + 50), Image.ANTIALIAS)
			image.paste(leaf_rsz, (150 - 25, self.pos_y - 25), leaf_rsz)	

class text:
	
	def __init__(self, start, duration, fading, phrase, position):
		self.startTime = start
		self.stopTime = start + duration + fading
		self.duration = duration
		self.fading = fading
		self.phrase = phrase 
		self.position = position

	def draw(self, frame, image):
		if(frame < self.startTime or frame >= self.stopTime):
			return
		idx = frame - self.startTime
		if idx > self.duration: 
			color = 255.*(1. - (idx - self.duration) / (self.fading - 1.))
			textMask = self.phrase(idx)
			textMask2 = Image.new("L", textMask.size, "black")
			textMask2.paste((color), (0, 0), textMask)
			image.paste("black", self.position, textMask2)
		else:
			textMask = self.phrase(idx)
			image.paste("black", self.position, textMask)

class leafText:
	def __init__(self, start, fading, phrase, position):
		self.startTime = start
		self.stopTime = start + fading + 5
		self.fading = fading
		self.phrase = phrase 
		self.position = position

	def draw(self, frame, image):
		if(frame < self.startTime or frame >= self.stopTime):
			return
		idx = frame - self.startTime
		if idx <= 5 : 
			color = int(255 / 5. * idx)
		else:
			color = int(255 - 255 / (self.fading - 1.) * (idx - 5))
		textMask = self.phrase(1000)
		textMask2 = Image.new("L", textMask.size, "black")
		textMask2.paste((color), (0, 0), textMask)
		image.paste("black", self.position, textMask2)

class zoom:

	def __init__(self, start):
		self.startTime = start
		self.stopTime = start + 100
		self.startRect = [0, 0, 1280, 720]
		self.endRect = [723, 255, 823, 323]

	def draw(self, frame, image):
		if(frame < self.startTime or frame >= self.stopTime):
			return
		idx = frame - self.startTime
		t = min(idx / 99., 1)
		rect = (int((1 - t) * self.startRect[0] + t * self.endRect[0]),
			int((1 - t) * self.startRect[1] + t * self.endRect[1]),
			int((1 - t) * self.startRect[2] + t * self.endRect[2]),
			int((1 - t) * self.startRect[3] + t * self.endRect[3]))
		im = image.crop(rect)
		im = im.resize((1280, 720), Image.ANTIALIAS)
		image.paste(im, (0, 0))

class evolve:

	def __init__(self, start):
		self.startTime = start
		self.stopTime = start + 690
		self.list = []
		self.list.append(still(start))
		self.list.append(emoticon(start + 230))
		self.list.append(animation3D(start + 430))
		self.list.append(zoom(start + 330))
		self.list.append(Transitions.blender(None, Image.open("./images/base2.png"), start + 670, 20))
		self.list.append(OneThought(start, 500, True))
		self.list.append(Transitions.blender(None, Image.open("./images/base13b.png"), start + 420, 10))
		self.list.append(text(start + 50, 190, 50, Phrases.getPhrase47, (110, 240)))
		self.list.append(text(start + 290, 90, 50, Phrases.getPhrase49, (250, 280)))
		self.list.append(leaf(start + 430, start + 440, 200, Image.open("./images/leaf1.png")))
		self.list.append(leafText(start + 445, 75, Phrases.getPhrase50, (300, 200)))
		self.list.append(leaf(start + 430, start + 510, 300, Image.open("./images/leaf2.png")))
		self.list.append(leafText(start + 515, 75, Phrases.getPhrase51, (300, 300)))
		self.list.append(leaf(start + 430, start + 590, 400, Image.open("./images/leaf3.png")))
		self.list.append(leafText(start + 595, 75, Phrases.getPhrase52, (300, 400)))
		#self.list.append(Transitions.blender(None, Image.open("./images/base14.png"), start + 670, 20))

	def draw(self, frame, image):
		if(frame < self.startTime or frame >= self.stopTime):
			return
		for obj in self.list:
			obj.draw(frame, image)
