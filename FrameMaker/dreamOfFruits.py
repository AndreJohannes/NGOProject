from PIL import Image
import aggdraw
import math
from Tools.phrases import Phrases
import Tools.transitions as Transitions


class still:

	def __init__(self, start):
		self.startTime = start
		self.stopTime = start + 450
		self.image =  Image.open("./images/base10.png")
	
	def draw(self, frame, image):
		if(frame < self.startTime or frame >= self.stopTime):
			return	
		image.paste(self.image, (0,0))

class text:

	def __init__(self, start, duration, phrase):
		self.startTime = start
		self.stopTime = start + duration
		self.phrase = phrase 

	def draw(self, frame, image):
		if(frame < self.startTime or frame >= self.stopTime):
			return
		idx = frame - self.startTime
		textMask = self.phrase(idx)
		image.paste("black",(810, 115),textMask)

class apple:

	def __init__(self, start, stop, position):
		self.startTime = start
		self.stopTime = stop
		self.position = position
		self.image = Image.open("./images/apple.png")

	def draw(self, frame, image):
		if(frame < self.startTime or frame >= self.stopTime):
			return
		idx = frame - self.startTime
		sz = min(idx, 35)
		apple = self.image.resize((sz,sz),Image.ANTIALIAS)
		image.paste(apple,(self.position[0]-sz/2,self.position[1]),apple)

class lupa:
	
	def __init__(self, start, stop, positionsAndPhrases):
		self.startTime = start
		self.stopTime = stop
		self.positionsAndPhrases = positionsAndPhrases
		self.lupa = Image.open("./images/lupa.png")
		self.mask = Image.open("./images/mask.png").convert("L")
		self.base = Image.open("./images/base10.png")
		self.apple = Image.open("./images/apple.png").resize((350,350),Image.ANTIALIAS)

	def draw(self, frame, image):
		if(frame < self.startTime or frame >= self.stopTime):
			return
		idx = frame - self.startTime
		[idx1,idx2] = divmod(idx, 40)
		k = math.pow(math.sin(math.pi /2. * idx2/39.),12 if idx1!=0 else 1)
		if idx1+2 > len(self.positionsAndPhrases):
			x = self.positionsAndPhrases[int(idx1)][0][0]
			y = self.positionsAndPhrases[int(idx1)][0][1]
		else:	
			x = int((1-k) * self.positionsAndPhrases[int(idx1)][0][0] + k*(self.positionsAndPhrases[int(idx1+1)][0][0]))
			y = int((1-k) * self.positionsAndPhrases[int(idx1)][0][1] + k*(self.positionsAndPhrases[int(idx1+1)][0][1]))
		area = self.base.crop((x-218/5,y-218/5,x+218/5,y+218/5))
		area = area.resize((218*2,2*218), Image.ANTIALIAS)
		for positionAndPhrase in self.positionsAndPhrases:
			ax = positionAndPhrase[0][0]
			ay = positionAndPhrase[0][1]
			textMask = positionAndPhrase[1]
			if textMask != None:
				pos=(43 - 5*(x-ax)-10,43 - 5*(y-ay))
				awt = self.apple.copy()
				awt.paste("white",(165-textMask.size[0]/2, 150),textMask)
				area.paste(awt, pos, awt)
		image.paste(area,(x-218,y-218),self.mask)
		image.paste(self.lupa,(x-254,y-244),self.lupa)


class evolve:

	def __init__(self, start):
		self.startTime = start
		self.stopTime = start + 430
		self.list = []
		positions = [(600,950),(400,237),(600,333),(396,380),(568,193),(529,352),(663,238),(409,304)]#,(723,372)]
		phrases = [None]
		phrases.append(["sustainable","economic","development"])
		phrases.append(["education","that","empowers"])
		phrases.append(["protected rights","and","justice"])
		phrases.append(["healthy relations","between","women and men"])
		phrases.append(["responsible","government"])
		phrases.append(["protected","environment"])
		phrases.append(["quality","health","care"])
		#phrases.append(["umbrella network","of","local NGOs"])
		self.list.append(still(start))
		self.list.append(text(start, 430, Phrases.getPhrase36))
		self.list.append(apple(start + 70, start + 410, positions[1] )) # could put the commands into a loop
		self.list.append(apple(start + 75, start + 410, positions[2] ))
		self.list.append(apple(start + 80, start + 410, positions[3] ))
		self.list.append(apple(start + 85, start + 410, positions[4] ))
		self.list.append(apple(start + 90, start + 410, positions[5] ))
		self.list.append(apple(start + 95, start + 410, positions[6] ))
		#self.list.append(apple(start + 100, start + 450, positions[7] ))		
		self.list.append(lupa(start + 110, start + 430, self.zipper(positions,phrases)))
		self.list.append(Transitions.pageFlip( Image.open("./images/base12.png").convert("RGBA"), None ,start+410,20, True))

	def draw(self, frame, image):
		if(frame < self.startTime or frame >= self.stopTime):
			return
		for obj in self.list:
			obj.draw(frame, image)

	def zipper(self, a,b):
		font = aggdraw.Font("white","./fonts/sans.ttf",28)
		phrases =  Phrases()
		return [[pos, phrases.makeImage_centered(texts, font) if texts != None else None] for pos,texts in zip(a,b)] 
