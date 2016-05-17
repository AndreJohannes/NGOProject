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
		image = Image.new("L",(1150,205),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "./fonts/adler.ttf",36)
		text = ["Hidalgo is a small, ruggedly beautiful state in"]
		text.append("central Mexico. There, indigenous citizens are")
		text.append("spread among three regions in which human")
		text.append("development levels are near the lowest in the")
		text.append("world:")
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
		font = aggdraw.Font("white", "./fonts/adler.ttf",36)
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
		font = aggdraw.Font("white", "./fonts/adler.ttf",36)
		text = ["-For centuries the indigenous people have been"]
		text.append(" separated by walls, dividing community from")
		text.append(" from community and the Region from the world.")
		text.append("             ")
		text.append("-The majority of the Region's people earn less")
		text.append("  than $96usd per month.")
		text.append("             ")
		text.append("-Less than 1% of homes possess a computer.")
		text.append("             ")
		text.append("-Communities rarely collaborate, municipalities")
		text.append(" even less.")
		text.append("             ")
		text.append("-Women average four grades of schooling")
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
		font = aggdraw.Font("white", "./fonts/adler.ttf",36)
		text = ["-Since 2013, Nahua, Otomi and Tepehua citizens"]
		text.append(" have defied the walls and build their own bottom-")
		text.append(" up rights-based movement.")
		text.append("             ")
		text.append("-In partnership with the Mexican NGO PSYDEH, in")
		text.append(" 2014 and 2015, a network of 500+ indigenous women")
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
		font = aggdraw.Font("white", "./fonts/adler.ttf",36)
		text = ["These seeds = learning about: "]
		text.append("             ")
		text.append("   - shared problems")
		text.append("             ")
		text.append("   - clarity on solutions")
		text.append("             ")
		text.append("   - leader disciplines to implement")
		text.append("     solutions")
		text.append("             ")
		text.append("   - rights & laws on which solutions are based")
		text.append("             ")		
		text.append("   - personal & communal autonomy")
	
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
		font = aggdraw.Font("white", "./fonts/adler.ttf",36)
		text = ["Where walls once existed, seeds have been planted"]
		text.append("and a tree grows.")
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
		font = aggdraw.Font("white", "./fonts/adler.ttf",36)
		text = ["This tree, our metaphor for sustainability"]
		text.append("symbolizes our work.")
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
		font = aggdraw.Font("white", "./fonts/adler.ttf",36)
		text = ["As our tree grows, it buds new life:"]
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
		font = aggdraw.Font("white", "./fonts/adler.ttf",36)
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
	def getPhrase46(i):
		image = Image.new("L",(1150,405),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "./fonts/adler.ttf",36)
		text = ["Still, as of May 2016, our tree is not strong enough"]
		text.append("to bear fruit. The foundation remains weak.")
		offset = 0 
		offsetY = 0
		for frag in text:
			d.text((10,offsetY),frag[0:max(i-offset,0)],font)
			offsetY += 40
			offset += len(frag)
		d.flush()
		return image


	@staticmethod
	def getPhrase47(i):
		image = Image.new("L",(1150,605),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "./fonts/adler.ttf",36)
		text = ["-Help us build our globally scalable model"]
		text.append(" for driving bottom-up sustainable development.")
		text.append("             ")
		text.append("-Team up with these women leaders and PSYDEH")
		text.append(" by supporting our first ever Crowdfunding")
		text.append(" campaign.")
		offset = 0 
		offsetY = 0
		for frag in text:
			d.text((10,offsetY),frag[0:max(i-offset,0)],font)
			offsetY += 40
			offset += len(frag)
		d.flush()
		return image				
	
	@staticmethod
	def getPhrase48(i):
		image = Image.new("L",(1150,605),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "adler.ttf",36)
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
			offsetY += 40
			offset += len(frag)
		d.flush()
		return image			

	@staticmethod
	def getPhrase49(i):
		image = Image.new("L",(1150,605),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "./fonts/adler.ttf",36)
		text = ["Our Campaign goal is $15,000usd."]
		text.append("This money will produce 3 critically")
		text.append("important initiatives.")
		offset = 0 
		offsetY = 0
		for frag in text:
			d.text((10,offsetY),frag[0:max(i-offset,0)],font)
			offsetY += 40
			offset += len(frag)
		d.flush()
		return image			

 
	@staticmethod
	def getPhrase50(i):
		image = Image.new("L",(1150,605),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "./fonts/adler.ttf",36)
		text = ["Conference linking Hidalgo's"]
		text.append("indigenous women leaders")
		offset = 0 
		offsetY = 0
		for frag in text:
			d.text((10,offsetY),frag[0:max(i-offset,0)],font)
			offsetY += 40
			offset += len(frag)
		d.flush()
		return image	


	@staticmethod
	def getPhrase51(i):
		image = Image.new("L",(1150,605),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "./fonts/adler.ttf",36)
		text = ["Training program for the Regional"]
		text.append("Cooperative of Indigenous Artisans.")
		offset = 0 
		offsetY = 0
		for frag in text:
			d.text((10,offsetY),frag[0:max(i-offset,0)],font)
			offsetY += 40
			offset += len(frag)
		d.flush()
		return image	

	@staticmethod
	def getPhrase52(i):
		image = Image.new("L",(1150,605),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "./fonts/adler.ttf",36)
		text = ["Narrative development program"]
		text.append("for the Network's women leaders.")
		offset = 0 
		offsetY = 0
		for frag in text:
			d.text((10,offsetY),frag[0:max(i-offset,0)],font)
			offsetY += 40
			offset += len(frag)
		d.flush()
		return image

	@staticmethod
	def getPhrase53(i):
		image = Image.new("L",(910,570),"black")
		d = aggdraw.Draw(image)
		font = aggdraw.Font("white", "adler.ttf",36)
		text = ["PSYDEH:"]
		text.append("At the table with our rural")
		text.append("and indigenous partners")
		text.append("in Mexico to:")
		text.append("     ")
		text.append("-boost citizen participiation")
		text.append("     ")
		text.append("-improve human security")
		text.append("     ")
		text.append("-build resilience")
		text.append("     ")
		text.append("-support responsible government")
		offset = 0 
		offsetY = 0
		for frag in text:
			d.text((10,offsetY),frag[0:max(i-offset,0)],font)
			offsetY += 40
			offset += len(frag)
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
