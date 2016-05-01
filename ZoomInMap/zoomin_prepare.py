from subprocess import call
import math
from PIL import Image

start = [0, 0, 1000, 680]
end = [530, 170, 660, 240]


# for i in range(0,170):
	
# 	k = 1- math.sin(math.pi *i/(2*169.))

# 	x1 =k* start[0] + (1-k) *end[0]
# 	y1 =k* start[1] + (1-k) *end[1]
# 	x2 =k* start[2] + (1-k) *end[2]
# 	y2 =k* start[3] + (1-k) *end[3]

# 	args = ["inkscape", "Mexico_Map.svg", 
# 		"--export-png=./images/preps/image{}a.png".format(i),
# 		"--export-area={}:{}:{}:{}".format(x1,y1,x2,y2),"-w=1280", "-h=720",
# 		"--export-background-opacity=255"]
# 	print "save image", str(i)	
# 	call(args)

# 	args = ["inkscape", "Hidalgo.svg", 
# 		"--export-png=./images/preps/image{}b.png".format(i),
# 		"--export-area={}:{}:{}:{}".format(x1,y1,x2,y2),"-w=1280", "-h=720",
# 		"--export-background-opacity=255"]
# 	print "save image", str(i)	
# 	call(args)

for i in range(0,170):
	k = 255.* max(i-130,0) / 39.;
	image1 = Image.open("./images/preps/image{}a.png".format(i))
	image2 = Image.open("./images/preps/image{}b.png".format(i))

	mask = Image.new("L",(1280,720),k)

	image1.paste(image2,(0,0), mask)

	image1.save("./images/preps/image{}.png".format(i),"png")


args = ["inkscape", "Hidalgo.svg", 
		"--export-png=./hidalgo.png",
		"--export-area={}:{}:{}:{}".format(530,170,660,240),"-w=1280", "-h=720",
		"--export-background-opacity=255"]
	#print "save image", str(i)	
call(args)

args = ["inkscape", "Otomi.svg", 
		"--export-png=./otomi.png",
		"--export-area={}:{}:{}:{}".format(530,170,660,240),"-w=1280", "-h=720",
		"--export-background-opacity=255"]
	#print "save image", str(i)	
call(args)

args = ["inkscape", "Mezquital.svg", 
		"--export-png=./mezquital.png",
		"--export-area={}:{}:{}:{}".format(530,170,660,240),"-w=1280", "-h=720",
		"--export-background-opacity=255"]
	#print "save image", str(i)	
call(args)

args = ["inkscape", "Huasteca.svg", 
		"--export-png=./huasteca.png",
		"--export-area={}:{}:{}:{}".format(530,170,660,240),"-w=1280", "-h=720",
		"--export-background-opacity=255"]
	#print "save image", str(i)	
call(args)