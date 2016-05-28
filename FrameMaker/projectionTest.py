from PIL import Image
import aggdraw
import math
import Tools.helpers as Helpers
import animation3D.perspective as Perspective
import animation3D.svgparser as SVGParser

class walker:

	def __init__(self):
		self.image = Image.open("./animation3D/walker/analy/frame{}.png".format(0)).convert("RGBA")

	def draw(self, data, image, idx):
		rect=[[0,0],[590,0],[590,590],[0,590]]
		data =  Helpers.find_coeffs(data,rect).tolist()
		im = Image.open("./animation3D/walker/analy/frame{}.png".format(min(max(0, idx), 107))).convert("RGBA")
		tm = im.transform((1280,720), Image.PERSPECTIVE, data, Image.BICUBIC)
		image.paste(tm, (0,0), tm)

class map:

	def __init__(self):
		self.parser = SVGParser.svgParse("./animation3D/Hidalgo.svg")

	def draw(self, caller, image):
		canvas = aggdraw.Draw(image)
		pen  = aggdraw.Pen("black", 0)
		regions = [[2, aggdraw.Brush("grey",255)]]
		regions.append([3,aggdraw.Brush((221, 63, 35),255)])
		regions.append([4,aggdraw.Brush((170, 136, 0),255)])
		regions.append([5,aggdraw.Brush((33,181,0),255)])
		for region in regions:
			brush = region[1]
			area = self.parser.get_path(region[0])
			path = []
			for coord in area:
				cc = caller([-100+coord[0],0,100-coord[1]])
				path.append(cc[0])
				path.append(cc[1])
			canvas.polygon(path,pen, brush)
		canvas.flush()

class box:

	def __init__(self, start):
		self.startTime = start
		self.perspective = Perspective.perspective()
		self.map = map()
		self.walker = walker()
		self.plane_walker1 = [[-85,-100,-9],[5,-100,-4],[5,0,-4],[-85,0,-9]]	
		self.plane_walker2 = [[94,-100,9],[5,-100,-4],[5,0,-4],[94,0,9]]	
		self.plane_walker3 = [[58,-100,69],[5,-100,-4],[5,0,-4],[58,0,69]]

	def draw(self, frame, image):
		image.paste((248,240,118),(0,0,1280,720))
		idx = frame - self.startTime
		zoom = max(2, min(5., (idx/15.)))
		ang = min(idx,70)
		caller = lambda x : self.projectAndRotate(ang, x ,zoom)
		self.map.draw(caller, image)
		plane = []
		for point in self.plane_walker1:
			plane.append(self.projectAndRotate(ang, point, zoom))
		self.walker.draw(plane, image, idx)
		plane = []
		for point in self.plane_walker2:
			plane.append(self.projectAndRotate(ang, point, zoom))
		self.walker.draw(plane, image, idx)
		plane = []
		for point in self.plane_walker3:
			plane.append(self.projectAndRotate(ang, point, zoom))
		self.walker.draw(plane, image, idx)

	def projectAndRotate(self, idx, data, zoom):
		return self.perspective.project(self.perspective.rotX(math.pi*(90-idx)/180.,self.perspective.rotY(math.pi*0/180.,data)), zoom)

