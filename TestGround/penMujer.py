from PIL import Image
from PIL import ImageDraw
import aggdraw
import math
import random
from Tools.phrases import Phrases
from Tools.flags import Flags
import Tools.tools as Tools

class OneThought:

	def __init__(self, startTime, image, pos_x, left):
		self.bubble = Tools.MovingBubble(pos_x,163,10,startTime, 20, left)
		pos_x += -100 if left else 100
		self.rectangualar = Tools.MorphingTextBox(image, pos_x,139,20,startTime+20, True)

	def draw(self, frame, image):
		self.bubble.draw(frame, image)
		self.rectangualar.draw(frame, image)	


class think:

	def __init__(self,start):
		self.startTime = start
		self.stopTime = start + 156
		self.transition = start + 130
		self.image = Image.open("./images/base2.png")
		font = aggdraw.Font("white", "./fonts/font1.ttf",46)
		phrase = Phrases().makeImage(["If I could remove","some blocks...?"],font)
		self.thoughts = [OneThought(start + 0, phrase, 500, True)]
		phrase = Phrases().makeImage(["AND if the person on the","other side does the same..."],font)
		self.thoughts.append(OneThought(start + 30, phrase, 877, False))
		phrase = Phrases().makeImage(["We can actually grow","the sustainable!"],font)
		self.thoughts.append(OneThought(start + 60, phrase, 500, True))

		#self.thoughts.append(Tools.ThoughtfulTransition(start + 290,Image.open("./images/base2.png") , 380))

	def draw(self, frame, image):
		if(frame < self.startTime or frame >= self.stopTime):
 			return
 	
 		if frame >= self.transition:
 			idx = frame - self.transition
 			base = Image.open("./images/slider/image"+ "{:02d}".format(max(min(idx,28),0)) +".png")
 			image.paste(base,(0,0))
 			dic = {10:1221,11:1196,12:1153,13:1096,14:1022,15:952,16:874,17:797,18:724,19:646,20:562,21:476,22:391,23:297,24:208,25:80}
 			if(dic.has_key(idx)):
				base2 = Image.open("./images/base3.png")
				mask = Image.new("L",(1280,720),"white")
				mask.paste("black",(0,0,dic[idx],720))
				image.paste(base2,(0,0),mask)
		else:
			image.paste(self.image, (0,0))

 		for though in self.thoughts:
 			though.draw(frame, image)