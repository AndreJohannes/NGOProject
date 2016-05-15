import random
import datetime
import Tkinter
from PIL import Image, ImageTk, ImageDraw
import aggdraw
import bubbleWorld
import titleOverlay
import flippingWorld
import walkIn
import buildWall

class Obj:
 
	def __init__(self):
 		self.startTime = random.randint(1, 6000)
 		self.stopTime = self.startTime + random.randint(10, 200)
 		self.position = (random.randint(0, 1280), random.randint(0, 720))
 		self.radius = random.randint(10, 50)

 	def draw(self, frame, image):
 		if(frame < self.startTime or frame > self.stopTime):
 			return
 		d = aggdraw.Draw(image)
		p = aggdraw.Pen("black", 2.5)
		pos_x = self.position[0]
		pos_y = self.position[1]
		radius = self.radius
		d.ellipse((pos_x-radius, pos_y-radius, pos_x+radius, pos_y+radius), p)
		d.flush()	

class Main:

	def __init__(self):
		self.frame = 395
		self.save = False
		self.photo_image = None
		self.list = []
		self.list.append(bubbleWorld.bubble(0,120,200))
		self.list.append(bubbleWorld.bubble(25,95,200))
		self.list.append(bubbleWorld.bubble(51,69,200))
		self.list.append(bubbleWorld.bubble(77,43,43))
		self.list.append(bubbleWorld.bubble(103,17,200))
		self.list.append(bubbleWorld.worldBubble(120,180))
		self.list.append(titleOverlay.title(230,120,(0,0)))
		self.list.append(flippingWorld.world(300))
		self.list.append(walkIn.walk(300))
		self.list.append(buildWall.wall(396))
		##for i in range(0,200):
		##	self.list.append(Obj())

	def key_callback(self, value):
		if(value.keycode == 113):
			self.frame -= 1
		elif(value.keycode == 114):
			self.frame += 1
		elif(value.char == "s"):
			self.save = not self.save
		image = Image.new("RGBA",(1280,720),"white")
		#base = Image.open("../Movie/images/image{}.png".format(self.frame))
		#image.paste(base,(0,0))
		for obj in self.list:
			obj.draw(self.frame, image)
		if self.save:
			image.save("./frames/frame{}.png".format(self.frame),"png")	
		d = ImageDraw.Draw(image)
		d.text((0,0),"frame: {}".format(self.frame),"black")
		d.text((0,8),"time: {}".format(datetime.timedelta(seconds=self.frame/25)),"black")
		d.text((0,16),"save: {}".format("on" if self.save else "off"),"black")
		self.photo_image = ImageTk.PhotoImage(image)
		canvas.create_image(640,360, image = self.photo_image)



app = Tkinter.Tk()
main = Main()
app.bind("<Key>", main.key_callback)
canvas = Tkinter.Canvas(app,width=1280, height=720)
canvas.pack()
#app.mainloop()