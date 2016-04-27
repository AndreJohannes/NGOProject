from PIL import Image
from PIL import ImageDraw
import aggdraw
import math

class Phrases:

	def __init__(self):
		self.dict = {}
		self.dict["1"] = Phrases.getPhrase1()
		self.dict["2"] = Phrases.getPhrase2()
		self.dict["3"] = Phrases.getPhrase3()
		self.dict["4"] = Phrases.getPhrase4()
		self.dict["5"] = Phrases.getPhrase5() 
		self.dict["6"] = Phrases.getPhrase6() 
		self.dict["7"] = Phrases.getPhrase7() 
		self.dict["8"] = Phrases.getPhrase8() 
		self.dict["9"] = Phrases.getPhrase9()
		self.dict["10"] = Phrases.getPhrase10()
		self.dict["11"] = Phrases.getPhrase11()
		self.dict["12"] = Phrases.getPhrase12()
		self.dict["13"] = Phrases.getPhrase13() 
		self.dict["14"] = Phrases.getPhrase14() 
		self.dict["15"] = Phrases.getPhrase15()  
		self.dict["16"] = Phrases.getPhrase16()
		self.dict["17"] = Phrases.getPhrase17()
		self.dict["18"] = Phrases.getPhrase18()
		self.dict["19"] = Phrases.getPhrase19()
		self.dict["20"] = Phrases.getPhrase20()
		self.dict["21"] = Phrases.getPhrase21()
		

	def getPhrase(self, name):
		return self.dict[name]

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
		d.text((30,25), "person!", font)
		d.flush()
		return image			

	@staticmethod
	def getPhrase5():
		image = Image.new("L",(140,60),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "font1.ttf",36)
		d.text((10, 0), "I am only one", font)
		d.text((30,25), "person!", font)
		d.flush()
		return image

	@staticmethod
	def getPhrase6():
		image = Image.new("L",(130,60),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "font1.ttf",36)
		d.text((10, 0), "North", font)
		d.text((30,25), "Americans", font)
		d.flush()
		return image

	@staticmethod
	def getPhrase7():
		image = Image.new("L",(90,45),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "font1.ttf",36)
		d.text((10, 5), "Germans", font)
		d.flush()
		return image

	@staticmethod
	def getPhrase8():
		image = Image.new("L",(120,45),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "font1.ttf",36)
		d.text((10, 5), "Guatemalans", font)
		d.flush()
		return image

	@staticmethod
	def getPhrase9():
		image = Image.new("L",(90,45),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "font1.ttf",36)
		d.text((10, 5), "Russians", font)
		d.flush()
		return image

	@staticmethod
	def getPhrase10():
		image = Image.new("L",(100,45),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "font1.ttf",36)
		d.text((10, 5), "Hondurans", font)
		d.flush()
		return image

	@staticmethod
	def getPhrase11():
		image = Image.new("L",(100,45),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "font1.ttf",36)
		d.text((10, 5), "Spaniards", font)
		d.flush()
		return image

	@staticmethod
	def getPhrase12():
		image = Image.new("L",(100,45),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "font1.ttf",36)
		d.text((10, 5), "Brazilians", font)
		d.flush()
		return image		

	@staticmethod
	def getPhrase13():
		image = Image.new("L",(80,45),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "font1.ttf",36)
		d.text((10, 5), "Scottish", font)
		d.flush()
		return image

	@staticmethod
	def getPhrase14():
		image = Image.new("L",(120,45),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "font1.ttf",36)
		d.text((10, 5), "Argentinians", font)
		d.flush()
		return image

	@staticmethod
	def getPhrase15():
		image = Image.new("L",(110,45),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "font1.ttf",36)
		d.text((10, 5), "Australians", font)
		d.flush()
		return image		

	@staticmethod
	def getPhrase16():
		image = Image.new("L",(90,45),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "font1.ttf",36)
		d.text((10, 5), "Nigerians", font)
		d.flush()
		return image

	@staticmethod
	def getPhrase17():
		image = Image.new("L",(120,60),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "font1.ttf",36)
		d.text((10, 0), "We are so", font)
		d.text((50,25), "different", font)
		d.flush()
		return image	

	@staticmethod
	def getPhrase18():
		image = Image.new("L",(120,60),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "font1.ttf",36)
		d.text((10, 0), "Different can", font)
		d.text((30,25), "be scary", font)
		d.flush()
		return image

	@staticmethod
	def getPhrase19():
		image = Image.new("L",(130,60),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "font1.ttf",36)
		d.text((10, 0), "The world is", font)
		d.text((50,25), "changing", font)
		d.flush()
		return image

	@staticmethod
	def getPhrase20():
		image = Image.new("L",(130,60),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "font1.ttf",36)
		d.text((10, 0), "Change is", font)
		d.text((30,25), "complicated", font)
		d.flush()
		return image

	@staticmethod
	def getPhrase21():
		image = Image.new("L",(150,95),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "font1.ttf",36)
		d.text((10, 0), "And those walls, ", font)
		d.text((30,25), "they are big", font)
		d.text((10,55), "and casy to build", font)
		d.flush()
		d.flush()
		return image

	@staticmethod
	def getPhrase22():
		image = Image.new("L",(260,175),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "font1.ttf",36)
		d.text((10, 0), "But what are people like", font)
		d.text((50,35), "on the other side?", font)
		d.text((10,65), "Difference seperates us, but", font)
		d.text((10,95), "it also makes us stronger, ", font)
		d.text((170,125), "doesnt it?", font)
		d.flush()
		d.flush()
		return image
