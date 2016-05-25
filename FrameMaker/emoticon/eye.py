import random
import datetime
import Tkinter
from PIL import Image, ImageTk, ImageDraw
import aggdraw
import math


#747 258
#764 293
#697 256

class eye:

	def __init__(self, start):
		self.image = Image.open("test1.png")
		self.eye_base = Image.new("RGBA",(55, 63), "white")	
		self.eye_left = Image.open("eye_left.png")
		self.eye_right = Image.open("eye_right.png")

	def draw(self, frame, image):
		image.paste(self.image, (0, 0))
		eye_base = self.eye_base.copy()
		center = (17, 35)
		canvas = aggdraw.Draw(eye_base)
		pen  = aggdraw.Pen("black", 0)
		brush = aggdraw.Brush("black",255);
		canvas.ellipse((17-12,35-12,17+12,35+12),pen, brush)
		pen  = aggdraw.Pen("black", 1)
		brush = aggdraw.Brush((248,249,118),255)
		lev = 44 * math.sin(frame/3.)
		canvas.ellipse((27.5-100,-90+lev-100,27.5+100,-90+lev+100),pen, brush)

		canvas.flush()
		eye_left = eye_base.copy()
		eye_left.paste(self.eye_left, (0,0), self.eye_left)
		eye_right = eye_base
		eye_right.paste(self.eye_right, (0,0), self.eye_right)
		image.paste(eye_left, (747, 258))
		image.paste(eye_right, (607, 256))

class Main:

	def __init__(self):
		self.frame = 0
		self.save = False
		self.photo_image = None
		self.list = []
		self.list.append(eye(0))

	def key_callback(self, value):
		if(value.keycode == 113):
			self.frame -= 1
		elif(value.keycode == 114):
			self.frame += 1
		elif(value.char == "s"):
			self.save = not self.save
		image = Image.new("RGBA",(1280,720),"white")
		for obj in self.list:
			obj.draw(self.frame, image)
		if self.save:
			image.save("./eyeFrames/frame{}.png".format(self.frame),"png")	
		d = ImageDraw.Draw(image)
		d.text((0,0),"frame: {}".format(self.frame),"black")
		d.text((0,8),"time: {}".format(datetime.timedelta(seconds=self.frame/25)),"black")
		d.text((0,16),"save: {}".format("on" if self.save else "off"),"black")
		self.photo_image = ImageTk.PhotoImage(image)
		canvas.create_image(640,360, image = self.photo_image)

	def save_frames(self, startFrame, stopFrame):
		for frame in range(startFrame, stopFrame+1):
			image = Image.new("RGBA",(1280,720),"white")
			for obj in self.list:
				obj.draw(frame, image)
			print "saving frame: {}".format(frame)
			image.save("./eyeFrames/frame{}.png".format(frame),"png")	

app = Tkinter.Tk()
app.title("PSYDEH")
main = Main()
app.bind("<Key>", main.key_callback)
canvas = Tkinter.Canvas(app,width=1280, height=720)
canvas.pack()


