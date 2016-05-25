from PIL import Image
from PIL import ImageDraw
import aggdraw
import math
import random



class bezier:

	def __init__(self,data):
		self.data = data

	def draw(self, image):
		[x1, x2, xc] = self.data
		coords = []
		res = 50
		for i in range(0,res+1):
			t = i/(1.0*res)
			p0 = [(1-t) * x1[0] + t * xc[0], (1-t) * x1[1] + t * xc[1]]
			p1 = [(1-t) * xc[0] + t * x2[0], (1-t) * xc[1] + t * x2[1]]
			x = [(1-t) * p0[0] + t* p1[0], (1-t) * p0[1] + t* p1[1]]
			coords.append(x[0])
			coords.append(x[1])
		canvas = aggdraw.Draw(image)
		pen  = aggdraw.Pen("black", 11)
		brush = aggdraw.Brush((255,255,150),230);
		canvas.line(coords,pen)
		canvas.flush()

	def get_coordinates(self, res):
		[x1, x2, xc] = self.data
		coords = []
		for i in range(0,res+1):
			t = i/(1.0*res)
			p0 = [(1-t) * x1[0] + t * xc[0], (1-t) * x1[1] + t * xc[1]]
			p1 = [(1-t) * xc[0] + t * x2[0], (1-t) * xc[1] + t * x2[1]]
			x = [(1-t) * p0[0] + t* p1[0], (1-t) * p0[1] + t* p1[1]]
			coords.append(x)
		return coords

class specialBezier:
	
	def __init__(self,data, width =0.2):
		[x1, x2, x3] = data
		self.distances = [self.get_distance(x1, x2), self.get_distance(x2, x3)]
		xd1 = [x2[0] + width*(x1[0] - x3[0]), x2[1] + width*( x1[1] - x3[1])]
		xd2 = [x2[0] - width*(x1[0] - x3[0]), x2[1] - width*( x1[1] - x3[1])]
		self.bez1 = bezier([x1, x2, xd1])
		self.bez2 = bezier([x2, x3, xd2])
		self.points =  [x1, x2, x3, xd1, xd2]

	def draw(self, image):
		self.bez1.draw(image)
		self.bez2.draw(image)	

	def get_coordinates(self, res):
		coords = self.bez1.get_coordinates(int(res * self.distances[0]/(self.distances[0]+self.distances[1])))
		coords.pop()
		coords.extend(self.bez2.get_coordinates(int(res * self.distances[1]/(self.distances[0]+self.distances[1]))))
		return coords

	def get_points(self):
		return self.points

	def get_distance(self, x1, x2):
		return math.sqrt((x1[0]-x2[0])*(x1[0]-x2[0])+(x1[1]-x2[1])*(x1[1]-x2[1]))

class hand:

	def __init__(self, flip = False):
		self.image = Image.open("./hand.png") if not flip else Image.open("./hand.png").transpose(Image.FLIP_LEFT_RIGHT) 


	def draw(self, image, position, ang):
		im = self.image.rotate(ang,  expand=1)
		size = im.size
		image.paste(im, (position[0] -size[0]/2, position[1]- size[1]/2), im)
 


bez1 = specialBezier([[787, 489], [819,465] ,[715, 493]], 1.0)
bez2 = specialBezier([[972, 646],[966,667], [916,666]], 1.0)
coords1 = bez1.get_coordinates(25)
coords2 = bez2.get_coordinates(25)
coords = zip(coords1, coords2)
coords_right = [[[coord[0][0]+random.randint(-2,2),coord[0][1]+random.randint(-2,2)],[coord[1][0]+random.randint(-2,2),coord[1][1]+random.randint(-2,2)]]  for coord in coords]
bez1 = specialBezier([[684, 750], [630,663] ,[710, 493]], 1.0)
bez2 = specialBezier([[501, 652],[481,667], [520,666]], 1.0)
coords1 = bez1.get_coordinates(25)
coords2 = bez2.get_coordinates(25)
coords = zip(coords1, coords2)
coords_left = [[[coord[0][0]+random.randint(-2,2),coord[0][1]+random.randint(-2,2)],[coord[1][0]+random.randint(-2,2),coord[1][1]+random.randint(-2,2)]]  for coord in coords]

coords = zip(coords_right, coords_left)
last = coords.pop()
for i in range(1, 30):
	coords.append(last)

hand_left = hand()
hand_right = hand(True)
idx = 0
for coord in coords:
	im = Image.open("./test1.png")
	bez = specialBezier([[715,584],coord[0][1],coord[0][0]])
	bez.draw(im)
	points =  bez.get_points()
	rad = math.atan2(points[2][0]-points[4][0], points[2][1]-points[4][1])
	hand_left.draw(im, (int(points[2][0]),int(points[2][1])), 90+rad / math.pi * 180)
	bez = specialBezier([[715,584],coord[1][1],coord[1][0]])
	bez.draw(im)
	points =  bez.get_points()
	rad = math.atan2(points[2][0]-points[4][0], points[2][1]-points[4][1])
	hand_right.draw(im, (int(points[2][0]),int(points[2][1])), (-90+rad / math.pi * 180))
	im.save("./bezierFrames/frame{}.png".format(idx),"png")
	idx+=1
#im = Image.open("./test1.png")
#bez = specialBezier([[715,584],[916, 666],[737,493]])
#bez.draw(im)
#im.show()
