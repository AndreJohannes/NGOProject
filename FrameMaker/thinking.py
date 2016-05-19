from PIL import Image
from PIL import ImageDraw
import aggdraw
import math
import random
from Tools.phrases import Phrases
from Tools.flags import Flags
import Tools.tools as Tools

class think:

	def __init__(self,start):
		self.startTime = start
		self.stopTime = start + 380
		self.image = Image.open("./images/base1.png")
		d = aggdraw.Draw(self.image)
		p = aggdraw.Pen("black", 8.46666)
		d.ellipse((640-315,596,640+315,596),p)
		d.flush()
		font = aggdraw.Font("white", "./fonts/font1.ttf",46)
		phrase = Phrases().makeImage(["We build a wall?","     Really?"],font)
		self.thoughts = [Tools.OneThought(start + 0, phrase, 380)]
		phrase = Phrases().makeImage(["What are people like","on the other side?"],font)
		self.thoughts.append(Tools.OneThought(start + 30, phrase, 945))
		phrase = Phrases().makeImage(["American"],font)
		self.thoughts.append(Tools.OneThought(start + 60, phrase, 380))
		phrase = Phrases().makeImage(["Mexican"],font)
		self.thoughts.append(Tools.OneThought(start + 90, phrase, 945))
		phrase = Phrases().makeImage(["Latinos, Europeans","  or Asians"],font)
		self.thoughts.append(Tools.OneThought(start + 120, phrase, 380))
		phrase = Phrases().makeImage(["We are so","different."],font)
		self.thoughts.append(Tools.OneThought(start + 150, phrase, 945))
		phrase = Phrases().makeImage(["All walls are made","of blocks."],font)
		self.thoughts.append(Tools.OneThought(start + 180, phrase, 380))
		phrase = Phrases().makeImage(["Violence, fear, poverty,"," ignorance"],font)
		self.thoughts.append(Tools.OneThought(start + 210, phrase, 945))
		phrase = Phrases().makeImage(["These blocks divide."],font)
		self.thoughts.append(Tools.OneThought(start + 240, phrase, 380))

		self.thoughts.append(Tools.OneFlag(start + 100, start + 170, "america", 462, 349))
		self.thoughts.append(Tools.OneFlag(start + 130, start + 200, "mexican", 826, 349))
		
		self.thoughts.append(Tools.OneFlag(start + 150, start + 200, "argentina", 462, 349))
		self.thoughts.append(Tools.OneFlag(start + 160, start + 230, "australia", 462, 349))
		self.thoughts.append(Tools.OneFlag(start + 170, start + 260, "spain", 462, 349))
		self.thoughts.append(Tools.OneFlag(start + 180, start + 300, "japanese", 462, 349))
		self.thoughts.append(Tools.OneFlag(start + 190, start + 380, "united", 462, 349))

		self.thoughts.append(Tools.OneFlag(start + 175, start + 245, "british", 826, 349))
		self.thoughts.append(Tools.OneFlag(start + 185, start + 275, "honduras", 826, 349))
		self.thoughts.append(Tools.OneFlag(start + 195, start + 315, "russia", 826, 349))
		self.thoughts.append(Tools.OneFlag(start + 205, start + 380, "united", 826, 349))

		self.thoughts.append(Tools.ThoughtfulTransition(start + 290,Image.open("./images/base2.png") , 380))


	def draw(self, frame, image):
		if(frame < self.startTime or frame >= self.stopTime):
 			return
 		image.paste(self.image, (0,0))	
 		for though in self.thoughts:
 			though.draw(frame, image)

