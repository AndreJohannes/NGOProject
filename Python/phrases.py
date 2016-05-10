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
	def getPhrase2():
		image = Image.new("L",(140,60),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "font1.ttf",36)
		d.text((10, 0), "We build a wall?", font)
		d.text((30,25), "Really?", font)
		d.flush()
		return image

	@staticmethod
	def getPhrase3():
		image = Image.new("L",(190,60),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "font1.ttf",36)
		d.text((10, 0), "What are people like", font)
		d.text((30,25), "on the other side?", font)
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
		d.text((30,25), "person.", font)
		d.flush()
		return image			

	@staticmethod
	def getPhrase6():
		image = Image.new("L",(90,45),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "font1.ttf",36)
		d.text((10, 5), "American", font)
		d.flush()
		return image

	@staticmethod
	def getPhrase7():
		image = Image.new("L",(90,45),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "font1.ttf",36)
		d.text((10, 5), "Mexican", font)
		d.flush()
		return image

	@staticmethod
	def getPhrase8():
		image = Image.new("L",(110,45),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "font1.ttf",36)
		d.text((10, 5), "Argentinian", font)
		d.flush()
		return image

	@staticmethod
	def getPhrase9():
		image = Image.new("L",(70,45),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "font1.ttf",36)
		d.text((10, 5), "Briton", font)
		d.flush()
		return image

	@staticmethod
	def getPhrase10():
		image = Image.new("L",(70,45),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "font1.ttf",36)
		d.text((10, 5), "German", font)
		d.flush()
		return image

	@staticmethod
	def getPhrase11():
		image = Image.new("L",(90,45),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "font1.ttf",36)
		d.text((10, 5), "Spaniard", font)
		d.flush()
		return image

	@staticmethod
	def getPhrase12():
		image = Image.new("L",(100,45),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "font1.ttf",36)
		d.text((10, 5), "Japanese", font)
		d.flush()
		return image

	@staticmethod
	def getPhrase13():
		image = Image.new("L",(50,45),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "font1.ttf",36)
		d.text((10, 5), "Kiwi", font)
		d.flush()
		return image		

	@staticmethod
	def getPhrase14():
		image = Image.new("L",(120,60),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "font1.ttf",36)
		d.text((10, 0), "We are so", font)
		d.text((50,25), "different.", font)
		d.flush()
		return image	

	@staticmethod
	def getPhrase15():
		image = Image.new("L",(130,60),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "font1.ttf",36)
		d.text((10, 0), "The world", font)
		d.text((50,25), "changes.", font)
		d.flush()
		return image

	@staticmethod
	def getPhrase16():
		image = Image.new("L",(180,60),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "font1.ttf",36)
		d.text((10, 0), "Differences and", font)
		d.text((30,25), "change are scary.", font)
		d.flush()
		return image


	@staticmethod
	def getPhrase17():
		image = Image.new("L",(210,60),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "font1.ttf",36)
		d.text((10, 0), "But what are people like", font)
		d.text((50,25), "on the other side?", font)
		d.flush()
		return image

	@staticmethod
	def getPhrase18():
		image = Image.new("L",(170,60),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "font1.ttf",36)
		d.text((10, 0), "All walls are made", font)
		d.text((20,25), "of blocks.", font)
		d.flush()
		return image	

	@staticmethod
	def getPhrase19():
		image = Image.new("L",(280,70),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "font1.ttf",36)
		d.text((10, 0), "Violence, fear, poverty, ignorance", font)
		d.text((20,25), "and technology isolation,", font)
		d.flush()
		return image

	@staticmethod
	def getPhrase20():
		image = Image.new("L",(260,30),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "font1.ttf",36)
		d.text((10, 0), "These blocks devide.", font)
		d.flush()
		return image

	@staticmethod
	def getPhrase21():
		image = Image.new("L",(220,75),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "font1.ttf",36)
		d.text((10, 0), "If I could begin taking the ", font)
		d.text((20,35), "blocks from the wall...?", font)
		d.flush()
		return image	

	@staticmethod
	def getPhrase22():
		image = Image.new("L",(300,105),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "font1.ttf",36)
		d.text((10, 0), "If the person on the other side does ", font)
		d.text((20,35), "the same, together, we could build", font)
		d.text((20,65), "the sustainable and beautiful.", font)
		d.flush()
		return image	

	@staticmethod
	def getPhrase23():
		image = Image.new("L",(260,75),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "font1.ttf",36)
		d.text((10, 0), "We ARE better in collaboration.", font)
		d.text((140, 35), "It is science!", font)
		d.flush()
		return image

	@staticmethod
	def getPhrase24(i):
		image = Image.new("L",(1150,205),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "adler.ttf",36)
		text = ["Hidalgo is a small, ruggedly beautiful state in"]
		text.append("central Mexico. There, a large indigenous popu-")
		text.append("lation is spread among three regions in which")
		text.append("human development levels are near the lowest ")
		text.append("in the world.")
		offset = 0 
		offsetY = 0
		for frag in text:
			d.text((10,offsetY),frag[0:max(i-offset,0)],font)
			offsetY += 40
			offset += len(frag)
		d.flush()
		return image	

	@staticmethod
	def getPhrase25(i):
		image = Image.new("L",(850,95),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "adler.ttf",36)
		text = [u"In the Otomi-Tepehua region"]
		text.append("sit four majority indigenous areas.")
		offset = 0 
		offsetY = 0
		for frag in text:
			d.text((10,offsetY),frag[0:max(i-offset,0)],font)
			offsetY += 40
			offset += len(frag)
		d.flush()
		return image	

	@staticmethod
	def getPhrase26(i):
		image = Image.new("L",(1150,905),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "adler.ttf",36)
		text = ["-For centuries the Region's indigenous citizens"]
		text.append(" have been seperated by walls, dividing community")
		text.append(" from community and the Region from the world.")
		text.append("             ")
		text.append("-As many as 86% of the Region's people earn less")
		text.append("  than $96usd per month.")
		text.append("             ")
		text.append("-Less than 1% of homes possess a computer.")
		text.append("             ")
		text.append("-Communities rarely collaborate, municipalities")
		text.append(" even less. Women average four grades of schooling")
		text.append(" and are not supported as leaders.")
		offset = 0 
		offsetY = 0
		for frag in text:
			d.text((10,offsetY),frag[0:max(i-offset,0)],font)
			offsetY += 40
			offset += len(frag)
		d.flush()
		return image

	@staticmethod
	def getPhrase27(i):
		image = Image.new("L",(1150,770),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "adler.ttf",36)
		text = ["-Since 2013, Nahua, Otomi and Tepehua citizens"]
		text.append(" have defied the walls and build their own bottom-")
		text.append(" up rights-based movement.")
		text.append("             ")
		text.append("-In partnership with the Mexican NGO PSYDEH, in")
		text.append(" 2014 and 2015, a network of 500+ indigenous woman")
		text.append(" from 35+ communities planted innovative seeds for")
		text.append(" their sustainable future.")
		offset = 0 
		offsetY = 0
		for frag in text:
			d.text((10,offsetY),frag[0:max(i-offset,0)],font)
			offsetY += 40
			offset += len(frag)
		d.flush()
		return image	

	@staticmethod
	def getPhrase28(i):
		image = Image.new("L",(1150,605),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "adler.ttf",36)
		text = ["These seeds are in form of learning about: "]
		text.append("             ")
		text.append("   - shared realities")
		text.append("             ")
		text.append("   - clarity on solutions to problems")
		text.append("             ")
		text.append("   - leader disciplines needed to implement")
		text.append("     solutions")
		text.append("             ")
		text.append("   - rights & laws on which solutions are based")
		text.append("             ")		
		text.append("   - personal & communal autonomy, including ")
		text.append("     how to negociate with government")
	
		offset = 0 
		offsetY = 0
		for frag in text:
			d.text((10,offsetY),frag[0:max(i-offset,0)],font)
			offsetY += 40
			offset += len(frag)
		d.flush()
		return image

	@staticmethod
	def getPhrase29(i):
		image = Image.new("L",(1150,205),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "adler.ttf",36)
		text = ["Where walls once existed, seeds have been planted"]
		text.append("and a symbolic tree grows.")
		offset = 0 
		offsetY = 0
		for frag in text:
			d.text((10,offsetY),frag[0:max(i-offset,0)],font)
			offsetY += 40
			offset += len(frag)
		d.flush()
		return image

	@staticmethod
	def getPhrase30(i):
		image = Image.new("L",(1150,205),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "adler.ttf",36)
		text = ["This tree is a universal metaphor for sustainable,"]
		text.append("resilient life, is that which represents our")
		text.append("movement's work.")
		offset = 0 
		offsetY = 0
		for frag in text:
			d.text((10,offsetY),frag[0:max(i-offset,0)],font)
			offsetY += 40
			offset += len(frag)
		d.flush()
		return image	

	@staticmethod
	def getPhrase31(i):
		image = Image.new("L",(1150,205),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "adler.ttf",36)
		text = ["As the tree grows, it has it has budded splendid"]
		text.append("new leaves:")
		offset = 0 
		offsetY = 0
		for frag in text:
			d.text((10,offsetY),frag[0:max(i-offset,0)],font)
			offsetY += 40
			offset += len(frag)
		d.flush()
		return image

	@staticmethod
	def getPhrase32(i):
		image = Image.new("L",(1150,205),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "sans.ttf",16)
		text = ["5 new indigenous"]
		text.append("    women-led")
		text.append("  organizations")
		offset = 0 
		offsetY = 0
		for frag in text:
			d.text((10,offsetY),frag[0:max(i-offset,0)],font)
			offsetY += 20
			offset += len(frag)
		d.flush()
		return image

	@staticmethod
	def getPhrase33(i):
		image = Image.new("L",(1150,205),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "sans.ttf",16)
		text = ["  Regional"]
		text.append("Development")
		text.append("  Agenda")
		offset = 0 
		offsetY = 0
		for frag in text:
			d.text((10,offsetY),frag[0:max(i-offset,0)],font)
			offsetY += 20
			offset += len(frag)
		d.flush()
		return image

	@staticmethod
	def getPhrase34(i):
		image = Image.new("L",(1150,205),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "sans.ttf",16)
		text = ["Regional "]
		text.append(" Cooperative")
		text.append("   of Artisans")
		offset = 0 
		offsetY = 0
		for frag in text:
			d.text((10,offsetY),frag[0:max(i-offset,0)],font)
			offsetY += 20
			offset += len(frag)
		d.flush()
		return image

	@staticmethod
	def getPhrase35(i):
		image = Image.new("L",(1150,205),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "sans.ttf",16)
		text = ["Annual Regional"]
		text.append("  Indigenous")
		text.append("   Women Forums")
		offset = 0 
		offsetY = 0
		for frag in text:
			d.text((10,offsetY),frag[0:max(i-offset,0)],font)
			offsetY += 20
			offset += len(frag)
		d.flush()
		return image

	@staticmethod
	def getPhrase36(i):
		image = Image.new("L",(570,405),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "adler.ttf",36)
		text = ["In just 1.5 years, "]
		text.append("the Region's")
		text.append("indigenous women")
		text.append("and PSYDEH have")
		text.append("dismantled walls,")
		text.append("planted seeds and") 
		text.append("dream of fruits")
		text.append("to come.")
		offset = 0 
		offsetY = 0
		for frag in text:
			d.text((10,offsetY),frag[0:max(i-offset,0)],font)
			offsetY += 40
			offset += len(frag)
		d.flush()
		return image

	@staticmethod
	def getPhrase37(i):
		image = Image.new("L",(175,130),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "sans.ttf",26)
		text = ["sustainable"]
		text.append(" economic")
		text.append("development")
		offset = 0 
		offsetY = 0
		for frag in text:
			d.text((10,offsetY),frag[0:max(i-offset,0)],font)
			offsetY += 30
			offset += len(frag)
		d.flush()
		return image

	@staticmethod
	def getPhrase38(i):
		image = Image.new("L",(150,130),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "sans.ttf",26)
		text = [" education"]
		text.append("      that")
		text.append(" empowers")
		offset = 0 
		offsetY = 0
		for frag in text:
			d.text((10,offsetY),frag[0:max(i-offset,0)],font)
			offsetY += 30
			offset += len(frag)
		d.flush()
		return image

	@staticmethod
	def getPhrase39(i):
		image = Image.new("L",(210,130),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "sans.ttf",26)
		text = ["protected rights"]
		text.append("       and")
		text.append("      justice")
		offset = 0 
		offsetY = 0
		for frag in text:
			d.text((10,offsetY),frag[0:max(i-offset,0)],font)
			offsetY += 30
			offset += len(frag)
		d.flush()
		return image
		
	@staticmethod
	def getPhrase40(i):
		image = Image.new("L",(220,130),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "sans.ttf",26)
		text = ["healthy relations"]
		text.append("     between")
		text.append("women and men")
		offset = 0 
		offsetY = 0
		for frag in text:
			d.text((10,offsetY),frag[0:max(i-offset,0)],font)
			offsetY += 30
			offset += len(frag)
		d.flush()
		return image		

	@staticmethod
	def getPhrase41(i):
		image = Image.new("L",(165,70),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "sans.ttf",26)
		text = ["responsible"]
		text.append("government ")
		offset = 0 
		offsetY = 0
		for frag in text:
			d.text((10,offsetY),frag[0:max(i-offset,0)],font)
			offsetY += 30
			offset += len(frag)
		d.flush()
		return image

	@staticmethod
	def getPhrase42(i):
		image = Image.new("L",(175,70),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "sans.ttf",26)
		text = ["  protected"]
		text.append("environment")
		offset = 0 
		offsetY = 0
		for frag in text:
			d.text((10,offsetY),frag[0:max(i-offset,0)],font)
			offsetY += 30
			offset += len(frag)
		d.flush()
		return image

	@staticmethod
	def getPhrase43(i):
		image = Image.new("L",(145,130),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "sans.ttf",26)
		text = ["quality"]
		text.append(" health")
		text.append("  care")
		offset = 0 
		offsetY = 0
		for frag in text:
			d.text((10,offsetY),frag[0:max(i-offset,0)],font)
			offsetY += 30
			offset += len(frag)
		d.flush()
		return image

	@staticmethod
	def getPhrase44(i):
		image = Image.new("L",(235,130),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "sans.ttf",26)
		text = ["umbrella network"]
		text.append("            of ")
		text.append("    local NGOs")
		offset = 0 
		offsetY = 0
		for frag in text:
			d.text((10,offsetY),frag[0:max(i-offset,0)],font)
			offsetY += 30
			offset += len(frag)
		d.flush()
		return image

	@staticmethod
	def getPhrase45(i):
		image = Image.new("L",(285,130),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "sans.ttf",26)
		text = ["free, prior & informed"]
		text.append("          consent")
		text.append("      on land use")
		offset = 0 
		offsetY = 0
		for frag in text:
			d.text((10,offsetY),frag[0:max(i-offset,0)],font)
			offsetY += 30
			offset += len(frag)
		d.flush()
		return image
	
	@staticmethod
	def getPhrase126(i):
		image = Image.new("L",(510,170),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "adler.ttf",36)
		d.text((10, 0), "PSYDEH:"[0:i], font)
		d.text((10,45), "At the table with our"[0:max(i-8,0)], font)
		d.text((10,85), "rural and indigenous"[0:max(i-29,0)], font)
		d.text((10,125), "partners in Mexico"[0:max(i-49,0)], font)
		d.flush()
		return image

	@staticmethod
	def getPhrase127(i):
		image = Image.new("L",(510,60),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "adler.ttf",40)
		d.text((10, 0), "www.psydeh.com"[0:max(i,0)], font)
		d.flush()
		return image

#Phrases.getPhrase26(50).show()	
