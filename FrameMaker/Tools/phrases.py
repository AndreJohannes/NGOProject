from PIL import Image
from PIL import ImageDraw
import aggdraw
import math

class Phrases:

	def __init__(self):
		self.image = Image.new("L",(1280,720),"black") 

	def getPhrase(self, name):
		return self.dict[name]


	@staticmethod
	def getPhrase24(i):
		image = Image.new("L",(1150,305),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "./fonts/calibrib.ttf",56)
		text = ["Hidalgo is a small, ruggedly beautiful state in"]
		text.append("central Mexico where its indigenous citizens live")
 		text.append("in three regions in which human development")
		text.append("levels are near the lowest in the world:")
		offset = 0 
		offsetY = 0
		for frag in text:
			d.text((10,offsetY),frag[0:max(i-offset,0)],font)
			offsetY += 60
			offset += len(frag)
		d.flush()
		return image

	@staticmethod
	def getPhrase25(i):
		image = Image.new("L",(1150,125),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "./fonts/calibrib.ttf",56)
		text = [u"In the Otom\u00ed-Tepehua region sit four majority"]
		text.append("indigenous areas.")
		offset = 0 
		offsetY = 0
		for frag in text:
			d.text((10,offsetY),frag[0:max(i-offset,0)],font)
			offsetY += 60
			offset += len(frag)
		d.flush()
		return image	

	@staticmethod
	def getPhrase26(i):
		image = Image.new("L",(1150,905),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "./fonts/calibrib.ttf",56)
		text = ["-For centuries, indigenous people are"]
		text.append(" separated by walls, dividing community from")
		text.append(" community and the Region from the world.")
		text.append("             ")
		text.append("-The majority of the Region's people earn less")
		text.append("  than $96usd per month.")
		text.append("             ")
		text.append("-Less than 1% of homes possess a computer.")
		text.append("             ")
		text.append("-Communities rarely collaborate, municipalities")
		text.append(" even less.")
		text.append("             ")
		text.append("-Women average three grades of schooling.")
		offset = 0 
		offsetY = 0
		for frag in text:
			d.text((10,offsetY),frag[0:max(i-offset,0)],font)
			offsetY += 60
			offset += len(frag)
		d.flush()
		return image

	@staticmethod
	def getPhrase27(i):
		image = Image.new("L",(1150,770),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "./fonts/calibrib.ttf",56)
		text = [u"-Since 2013, Nahua, Otom\u00ed and Tepehua citizens"]
		text.append(" defy the walls and build their own bottom-up")
		text.append(" rights-based movement.")
		text.append("             ")
		text.append("-In partnership with the Mexican NGO PSYDEH,")
		text.append(" in 2014 and 2015, a network of 500+ indigenous")
		text.append(" women from 35+ communities planted")
		text.append(" innovative seeds for their sustainable future.")
		offset = 0 
		offsetY = 0
		for frag in text:
			d.text((10,offsetY),frag[0:max(i-offset,0)],font)
			offsetY += 60
			offset += len(frag)
		d.flush()
		return image	

	@staticmethod
	def getPhrase28(i):
		image = Image.new("L",(1150,805),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "./fonts/calibrib.ttf",56)
		text = ["These seeds = learning about: "]
		text.append("             ")
		text.append("   - shared problems")
		text.append("             ")
		text.append("   - clarity on solutions")
		text.append("             ")
		text.append("   - leader disciplines to implement solutions")
		text.append("             ")
		text.append("   - rights & laws on which solutions are based")
		text.append("             ")		
		text.append("   - personal & communal autonomy")
	
		offset = 0 
		offsetY = 0
		for frag in text:
			d.text((10,offsetY),frag[0:max(i-offset,0)],font)
			offsetY += 60
			offset += len(frag)
		d.flush()
		return image

	@staticmethod
	def getPhrase29(i):
		image = Image.new("L",(1150,205),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "./fonts/calibrib.ttf",56)
		text = ["Where walls once existed, seeds are planted"]
		text.append("and a tree grows.")
		offset = 0 
		offsetY = 0
		for frag in text:
			d.text((10,offsetY),frag[0:max(i-offset,0)],font)
			offsetY += 60
			offset += len(frag)
		d.flush()
		return image

	@staticmethod
	def getPhrase30(i):
		image = Image.new("L",(1150,205),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "./fonts/calibrib.ttf",56)
		text = ["This tree, our metaphor for sustainability,"]
		text.append("symbolizes our work.")
		offset = 0 
		offsetY = 0
		for frag in text:
			d.text((10,offsetY),frag[0:max(i-offset,0)],font)
			offsetY += 60
			offset += len(frag)
		d.flush()
		return image	

	@staticmethod
	def getPhrase31(i):
		image = Image.new("L",(1150,205),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "./fonts/calibrib.ttf",56)
		#text = ["[This scene needs work.....]"]
		text = ["As our tree grows, it buds new life:"]
		offset = 0 
		offsetY = 0
		for frag in text:
			d.text((10,offsetY),frag[0:max(i-offset,0)],font)
			offsetY += 60
			offset += len(frag)
		d.flush()
		return image

	@staticmethod
	def getPhrase32(i):
		image = Image.new("L",(1150,205),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "./fonts/sans.ttf",26)
		text = ["         Umbrella"]
		text.append("  Network of")
		text.append("  five Indigenous")
		text.append("  Women-led")
		text.append("Organizations")
		offset = 0 
		offsetY = 0
		for frag in text:
			d.text((10,offsetY),frag[0:max(i-offset,0)],font)
			offsetY += 30
			offset += len(frag)
		d.flush()
		return image

	@staticmethod
	def getPhrase33(i):
		image = Image.new("L",(1150,205),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "./fonts/sans.ttf",26)
		text = ["  Regional"]
		text.append("Development")
		text.append("  Agenda")
		offset = 0 
		offsetY = 0
		for frag in text:
			d.text((10,offsetY),frag[0:max(i-offset,0)],font)
			offsetY += 30
			offset += len(frag)
		d.flush()
		return image

	@staticmethod
	def getPhrase34(i):
		image = Image.new("L",(1150,205),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "./fonts/sans.ttf",26)
		text = ["Regional "]
		text.append(" Cooperative")
		text.append("   of Artisans")
		offset = 0 
		offsetY = 0
		for frag in text:
			d.text((10,offsetY),frag[0:max(i-offset,0)],font)
			offsetY += 30
			offset += len(frag)
		d.flush()
		return image

	@staticmethod
	def getPhrase35(i):
		image = Image.new("L",(1150,205),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "./fonts/sans.ttf",26)
		text = ["Annual"]
		text.append("  Indigenous")
		text.append("      Women") 
		text.append("	       Forums")
		offset = 0 
		offsetY = 0
		for frag in text:
			d.text((10,offsetY),frag[0:max(i-offset,0)],font)
			offsetY += 30
			offset += len(frag)
		d.flush()
		return image

	@staticmethod
	def getPhrase36(i):
		image = Image.new("L",(570,405),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "./fonts/calibri.ttf", 46)
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
			offsetY += 46
			offset += len(frag)
		d.flush()
		return image

	@staticmethod
	def getPhrase46(i):
		image = Image.new("L",(1150,405),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "./fonts/calibrib.ttf",56)
		text = ["Still, as of May 2016, our tree is not strong"]
		text.append("enough to bear fruit. The foundation remains")
		text.append("weak.")
		offset = 0 
		offsetY = 0
		for frag in text:
			d.text((10,offsetY),frag[0:max(i-offset,0)],font)
			offsetY += 60
			offset += len(frag)
		d.flush()
		return image


	@staticmethod
	def getPhrase47(i):
		image = Image.new("L",(1150,605),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "./fonts/calibri.ttf",46)
		text = ["-Help us drive bottom-up sustainable development."]
		text.append("             ")
		text.append("-Team up with these women leaders and PSYDEH")
		text.append(" by supporting our first ever Crowdfunding campaign.")
		#text.append(" ")
		offset = 0 
		offsetY = 0
		for frag in text:
			d.text((10,offsetY),frag[0:max(i-offset,0)],font)
			offsetY += 50
			offset += len(frag)
		d.flush()
		return image				
	
	@staticmethod
	def getPhrase48(i):
		image = Image.new("L",(1150,605),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "calibri.ttf",46)
		text = ["While we pursue Mexican federal"]
		text.append("government aid, in-country politics")
		text.append("and economics tell us to reach out")
		text.append("to global citizens. We need help to") 
		text.append("build our globally scalable model")
		text.append("for driving bottom-up")
		text.append("sustainable development. ")
		offset = 0 
		offsetY = 0
		for frag in text:
			d.text((10,offsetY),frag[0:max(i-offset,0)],font)
			offsetY += 50
			offset += len(frag)
		d.flush()
		return image			

	@staticmethod
	def getPhrase49(i):
		image = Image.new("L",(1150,605),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "./fonts/calibri.ttf",46)
		text = ["Our Campaign goal is $15,000usd."]
		text.append("     ")
		text.append("This money will produce 4 projects.")
		offset = 0 
		offsetY = 0
		for frag in text:
			d.text((10,offsetY),frag[0:max(i-offset,0)],font)
			offsetY += 50
			offset += len(frag)
		d.flush()
		return image			

 
	@staticmethod
	def getPhrase50(i):
		image = Image.new("L",(1150,605),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "./fonts/calibri.ttf",46)
		text = ["Conference linking Hidalgo's"]
		text.append("indigenous women leaders")
		offset = 0 
		offsetY = 0
		for frag in text:
			d.text((10,offsetY),frag[0:max(i-offset,0)],font)
			offsetY += 50
			offset += len(frag)
		d.flush()
		return image	


	@staticmethod
	def getPhrase51(i):
		image = Image.new("L",(1150,605),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "./fonts/calibri.ttf",46)
		text = ["Training program for the Regional"]
		text.append("Cooperative of Indigenous Artisans.")
		offset = 0 
		offsetY = 0
		for frag in text:
			d.text((10,offsetY),frag[0:max(i-offset,0)],font)
			offsetY += 50
			offset += len(frag)
		d.flush()
		return image	

	@staticmethod
	def getPhrase52(i):
		image = Image.new("L",(1150,605),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "./fonts/calibri.ttf",46)
		text = ["Narrative development program"]
		text.append("for the Network's women leaders.")
		offset = 0 
		offsetY = 0
		for frag in text:
			d.text((10,offsetY),frag[0:max(i-offset,0)],font)
			offsetY += 50
			offset += len(frag)
		d.flush()
		return image

	@staticmethod
	def getPhrase53(i):
		image = Image.new("L",(910,570),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "./fonts/calibrib.ttf",46)
		text = ["PSYDEH:"]
		text.append("At the table with our rural and")
		text.append("indigenous partners in Mexico.")
		offset = 0 
		offsetY = 0
		for frag in text:
			d.text((10,offsetY),frag[0:max(i-offset,0)],font)
			offsetY += 50
			offset += len(frag)
		d.flush()
		return image


	@staticmethod
	def getPhrase54(i):
		image = Image.new("L",(790,160),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "./fonts/calibrib.ttf",46)
		text = []
		text.append("Visit PSYDEH's website for more")
		text.append("information: www.psydeh.com")
		offset = 0 
		offsetY = 0
		for frag in text:
			d.text((10,offsetY),frag[0:max(i-offset,0)],font)
			offsetY += 50
			offset += len(frag)
		d.flush()		
		return image

	@staticmethod
	def getPhrase55(i):
		image = Image.new("L",(1150,860),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "./fonts/calibrib.ttf",56)
		text = []
		text.append("-Join us in breaking down walls.")
		text.append("             ")
		text.append("-Support these three initiatives.")
		text.append("             ")
		text.append("-Help us grow our tree.")
		text.append("             ")
		text.append("-Global citizens thrive in informed collaboration!")
		offset = 0 
		offsetY = 0
		for frag in text:
			d.text((10,offsetY),frag[0:max(i-offset,0)],font)
			offsetY += 60
			offset += len(frag)
		d.flush()		
		return image

	def makeImage(self, listOfText, font):
		testCanvas = aggdraw.Draw(self.image)
		size_x = 0
		size_y = 0
		for text in listOfText:
			size = testCanvas.textsize(text, font)
			size_x = max(size_x, size[0])
			dy = size[1]
			size_y += size[1]
		image = Image.new("L",(int(size_x+20),int(size_y)),"black")
		d = aggdraw.Draw(image)
		yoffset = 0
		for text in listOfText:
			d.text((10, yoffset), text, font)
			yoffset += dy
		d.flush()
		return image

	def makeImage_centered(self, listOfText, font):
		testCanvas = aggdraw.Draw(self.image)
		size_x = 0
		size_y = 0
		for text in listOfText:
			size = testCanvas.textsize(text, font)
			size_x = max(size_x, size[0])
			dy = size[1]
			size_y += size[1]
		image = Image.new("L",(int(size_x+20),int(size_y)),"black")
		d = aggdraw.Draw(image)
		yoffset = 0
		for text in listOfText:
			size = testCanvas.textsize(text, font)
			d.text(((20+size_x-size[0])/2, yoffset), text, font)
			yoffset += dy
		d.flush()
		return image			

#Phrases.getPhrase26(50).show()	
