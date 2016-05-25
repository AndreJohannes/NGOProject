import datetime
import Tkinter
from PIL import Image, ImageTk, ImageDraw
import bubbleWorld
import thinking
import penMujer
import showMap
import informer
import treeGrowing
import dreamOfFruits
import stillWorking
import callForAction
import majesticTree
import roundTable

class moduleList:

	def __init__(self):
		self.list = []
		self.frame_counter = 0;

	def append(self, module):
		print "load module \"{}\" at frame {}".format(module.__name__,self.frame_counter)
		evolver = module.evolve(self.frame_counter)
		self.list.append(evolver)
		self.frame_counter = evolver.stopTime

	def get_list(self):
		return self.list

	def print_list(self):
		for instance in self.list:
			print "module \"{}\" at frame {}".format(instance.__module__,instance.startTime)

class Main:

	def __init__(self):
		self.frame = 3506
		self.save = False
		self.photo_image = None
		self.list = moduleList()
		self.list.append(bubbleWorld)
		self.list.append(thinking)#.think(430))
		self.list.append(penMujer)#.evolve(700))
		self.list.append(showMap)#.journey(856))
		self.list.append(informer)#.evolve(1441))
		self.list.append(treeGrowing)#.evolve(2611))
		#self.list.append(leafGrowing.evolve(3105))
		self.list.append(dreamOfFruits)#.evolve(2951))
		self.list.append(stillWorking)#.evolve(3380))
		self.list.append(callForAction)#.evolve(3505))
		self.list.append(majesticTree)#.evolve(4120))
		self.list.append(roundTable)#.evolve(4315))

	def key_callback(self, value):
		if(value.keycode == 113):
			self.frame -= 1
		elif(value.keycode == 114):
			self.frame += 1
		elif(value.keycode == 111):
			self.frame -= 10	
		elif(value.keycode == 116):
			self.frame += 10
		elif(value.char == "s"):
			self.save = not self.save
		image = Image.new("RGBA", (1280,720), "white")
		for obj in self.list.get_list():
			obj.draw(self.frame, image)
		if self.save:
			print "saving frame: {}".format(self.frame)
			image.save("./frames/frame{}.png".format(self.frame),"png")	
		d = ImageDraw.Draw(image)
		d.text((0,0), "frame: {}".format(self.frame), "black")
		d.text((0,8), "time: {}".format(datetime.timedelta(seconds=self.frame/25)), "black")
		d.text((0,16), "save: {}".format("on" if self.save else "off"), "black")
		self.photo_image = ImageTk.PhotoImage(image)
		canvas.create_image(640,360, image = self.photo_image)

	def save_frames(self, startFrame, stopFrame):
		for frame in range(startFrame, stopFrame + 1):
			image = Image.new("RGBA", (1280,720), "white")
			for obj in self.list.get_list():
				obj.draw(frame, image)
			print "saving frame: {}".format(frame)
			image.save("./frames/frame{}.png".format(frame),"png")	

	def list_modules(self):
		self.list.print_list()

app = Tkinter.Tk()
app.title("PSYDEH")
main = Main()
app.bind("<Key>", main.key_callback)
canvas = Tkinter.Canvas(app,width=1280, height=720)
canvas.pack()
#app.mainloop()