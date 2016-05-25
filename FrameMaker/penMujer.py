from PIL import Image
import aggdraw
from Tools.phrases import Phrases
import Tools.tools as Tools

class OneThought:

	def __init__(self, startTime, image, pos_x, left):
		self.bubble = Tools.MovingBubble(pos_x, 163, 10, startTime, 20, left)
		pos_x += -100 if left else 100
		self.rectangualar = Tools.MorphingTextBox(image, pos_x, 139, 20, startTime + 20, True)

	def draw(self, frame, image):
		self.bubble.draw(frame, image)
		self.rectangualar.draw(frame, image)	

class pensativo:

	def __init__(self, start):
		self.startTime = start
		self.stopTime = start + 130

	def draw(self, frame, image):
		if(frame < self.startTime or frame >= self.stopTime):
			return
		idx = frame - self.startTime
		im = Image.open("../Pensombre/images/pensativo/image{}.png".format(min(idx, 69))) 
		image.paste(im, (0, 0))

class rolling_tl:
	def __init__(self, start):
		self.startTime = start
		self.stopTime = start + 65

	def draw(self, frame, image):
		if(frame < self.startTime or frame >= self.stopTime):
			return
		idx = frame - self.startTime
		im = Image.open("../Pensombre/images/rollingeyes/topleft/image{}.png".format(min(idx, 5))).crop((0, 0, 800, 360)) 
		image.paste(im, (0, 0))

class rolling_tlb:
	def __init__(self, start):
		self.startTime = start
		self.stopTime = start + 20

	def draw(self, frame, image):
		if(frame < self.startTime or frame >= self.stopTime):
			return
		idx = frame - self.startTime
		im = Image.open("../Pensombre/images/rollingeyes/topleft/image{}.png".format(max(5 - idx, 0))).crop((0, 0, 800, 360)) 
		image.paste(im, (0, 0))

class slider:

	def __init__(self, start):
		self.startTime = start
		self.stopTime = start + 26

	def draw(self, frame, image):
		if(frame < self.startTime or frame >= self.stopTime):
			return
	
		idx = frame - self.startTime
		base = Image.open("./images/slider/image" + "{:02d}".format(max(min(idx, 26), 0)) + ".png")
		image.paste(base, (0, 0))
		dic = {10:1221, 11:1196, 12:1153, 13:1096, 14:1022, 15:952, 16:874, 17:797, 18:724, 19:646, 20:562, 21:476, 22:391, 23:297, 24:208, 25:80}
		if(dic.has_key(idx)):
			base2 = Image.open("./images/base3.png")
			mask = Image.new("L", (1280, 720), "white")
			mask.paste("black", (0, 0, dic[idx], 720))
			image.paste(base2, (0, 0), mask)


class evolve:

	def __init__(self, start):
		self.startTime = start
		self.stopTime = start + 156
		self.list = []
		self.list.append(pensativo(start))
		self.list.append(rolling_tl(start + 10))
		self.list.append(rolling_tlb(start + 75))
		self.list.append(slider(start + 130))
		font = aggdraw.Font("white", "./fonts/font1.ttf", 46)
		phrase = Phrases().makeImage(["If I could remove", "blocks from the wall...?"], font)
		self.list.append(OneThought(start + 0, phrase, 500, True))
		phrase = Phrases().makeImage(["AND if the person on the", "other side does the same..."], font)
		self.list.append(OneThought(start + 30, phrase, 877, False))
		phrase = Phrases().makeImage(["We can actually grow", "the sustainable!"], font)
		self.list.append(OneThought(start + 60, phrase, 500, True))
		# self.list.append(Transitions.pageFlip( Image.open("./images/base7.png"), Image.open("./images/base8.png").convert("RGBA"),start+400,20))

	def draw(self, frame, image):
		if(frame < self.startTime or frame >= self.stopTime):
			return
		for obj in self.list:
			obj.draw(frame, image)
