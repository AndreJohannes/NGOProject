from PIL import Image
from PIL import ImageDraw
import aggdraw
import math
import random
from Tools.phrases import Phrases
from Tools.flags import Flags
import Tools.tools as Tools
import Tools.transitions as Transitions
import Tools.helpers as Helpers

class perspective:

	def project(self, position):
		[x, y, z] = position
		C = 1000.
		return [640+ 5*x *C / (C + z), 460+ 5 * y * C /(C + z)]

	def rotX(self, rad, position):
		[x, y, z] = position
		cos = math.cos(rad)
		sin = math.sin(rad)
		return [x, y*cos - z * sin, z*cos + y * sin]

	def rotY(self, rad, position):
		[x, y, z] = position
		cos = math.cos(rad)
		sin = math.sin(rad)
		return [cos *x - sin *z , y, cos*z + sin*x]

class walker:
	def __init__(self):
		self.image = Image.open("../WalkIn/images/walkin-0.png").convert("RGBA")

	def draw(self, data, image, idx):
		rect=[[0,0],[1280,0],[1280,590],[0,590]]
		data =  Helpers.find_coeffs(data,rect).tolist()
		im = Image.open("../WalkIn/images/walkin-{}.png".format(min(max(0, idx), 37))).convert("RGBA")
		tm = im.transform((1280,720), Image.PERSPECTIVE, data, Image.BICUBIC)
		image.paste(tm, (0,0), tm)

class map:

	def __init__(self):
		self.image = Image.open("./test/map.png")

	def draw(self, data, image):
		rect=[[0,0],[0,512],[512,512],[512,0]]
		data =  Helpers.find_coeffs(data,rect).tolist()
		tm = self.image.transform((1280,720), Image.PERSPECTIVE, data, Image.BICUBIC)
		image.paste(tm, (0,0), tm)

class box:

	def __init__(self, start):
		self.startTime = start
		self.perspective = perspective()
		self.map = map()
		self.walker = walker()
		self.plane_map = [[-100,0,-100],[100,0,-100],[100,0,100],[-100,0,100]]
		self.plane_walker1 = [[-100,-100,0],[100,-100,0],[100,0,0],[-100,0,0]]	
		self.plane_walker2 = [[0,-100,-100],[0,-100,100],[0,0,100],[0,0,-100]]	

		#self.planes.append([[-100,0,-100],[100,0,-100],[100,0,100],[-100,0,100]])
		#self.planes.append([[-100,0,100],[100,0,100],[100,-100,100],[-100,-100,100]])
		#self.planes.append([[100,0,100],[100,0,-100],[100,-100,-100],[100,-100,100]])

	def draw(self, frame, image):
		idx = frame - self.startTime
		plane = []
		for point in self.plane_map:
			plane.append(self.projectAndRotate(20, point))
		self.map.draw(plane, image)
		plane = []
		for point in self.plane_walker1:
			plane.append(self.projectAndRotate(20, point))
		self.walker.draw(plane, image, idx/2)
		plane = []
		for point in self.plane_walker2:
			plane.append(self.projectAndRotate(20, point))
		self.walker.draw(plane, image, idx/2-10)

	def projectAndRotate(self, idx, data):
		return self.perspective.project(self.perspective.rotX(0.3,self.perspective.rotY(2*math.pi*idx/180.,data)))

