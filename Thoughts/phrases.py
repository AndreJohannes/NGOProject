from PIL import Image
from PIL import ImageDraw
import aggdraw
import math

class Phrases:

	@staticmethod
	def getPhrase1():
		image = Image.new("L",(120,60),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "font1.ttf",36)
		d.text((10, 0), "Build a wall?", font)
		d.text((30,25), "Really?", font)
		d.flush()
		return image

	@staticmethod
	def getPhrase2():
		image = Image.new("L",(190,60),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "font1.ttf",36)
		d.text((10, 0), "What are people like", font)
		d.text((30,25), "on the other side?", font)
		d.flush()
		return image

	@staticmethod
	def getPhrase3():
		image = Image.new("L",(170,40),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "font1.ttf",36)
		d.text((10, 0), "Should we engage?", font)
		d.flush()
		return image

	@staticmethod
	def getPhrase4():
		image = Image.new("L",(120,60),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "font1.ttf",36)
		d.text((10, 0), "How can we", font)
		d.text((30,25), "engage?", font)
		d.flush()
		return image

	@staticmethod
	def getPhrase5():
		image = Image.new("L",(140,60),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "font1.ttf",36)
		d.text((10, 0), "I am only one", font)
		d.text((30,25), "person?", font)
		d.flush()
		return image			


#Phrases.getPhrase1().show()
#Phrases.getPhrase2().show()
#Phrases.getPhrase3().show()
#Phrases.getPhrase4().show()
#Phrases.getPhrase5().show()
