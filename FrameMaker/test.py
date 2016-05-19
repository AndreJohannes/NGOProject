import random
import datetime
import Tkinter
from PIL import Image, ImageTk, ImageDraw
import aggdraw
import projectionTest

class Main:

	def __init__(self):
		self.frame = 0
		self.save = False
		self.photo_image = None
		self.list = []
		self.list.append(projectionTest.box(0))

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
			image.save("./test/frames/frame{}.png".format(self.frame),"png")	
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
			image.save("./test/frames/frame{}.png".format(frame),"png")	

app = Tkinter.Tk()
app.title("PSYDEH")
main = Main()
app.bind("<Key>", main.key_callback)
canvas = Tkinter.Canvas(app,width=1280, height=720)
canvas.pack()
#app.mainloop()