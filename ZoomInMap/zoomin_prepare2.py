from subprocess import call
import math
from PIL import Image

start = [530, 170, 660, 240]
end = [590,190, 640, 220]


iOffset = 510

# for i in range(0,70):
	
# 	k = 1- math.sin(math.pi *i/(2*69.))

# 	x1 =k* start[0] + (1-k) *end[0]
# 	y1 =k* start[1] + (1-k) *end[1]
# 	x2 =k* start[2] + (1-k) *end[2]
# 	y2 =k* start[3] + (1-k) *end[3]


# 	args = ["inkscape", "Otomi.svg", 
# 		"--export-png=./images/preps/image{}a.png".format(i + iOffset),
# 		"--export-area={}:{}:{}:{}".format(x1,y1,x2,y2),"-w=1280", "-h=720",
# 		"--export-background-opacity=255"]
# 	print "save image", str(i + iOffset)	
# 	call(args)

# 	args = ["inkscape", "Hidalgo.svg", 
# 		"--export-png=./images/preps/image{}b.png".format(i + iOffset),
# 		"--export-area={}:{}:{}:{}".format(x1,y1,x2,y2),"-w=1280", "-h=720",
# 		"--export-background-opacity=255"]
# 	print "save image", str(i + iOffset)	
# 	call(args)

#  	k = 255.* min(i/20.,1);
#  	image1 = Image.open("./images/preps/image{}a.png".format(i + iOffset))
#  	image2 = Image.open("./images/preps/image{}b.png".format(i + iOffset))

#  	mask = Image.new("L",(1280,720),k)
#  	image1.paste(image2,(0,0), mask)

#  	image1.save("./images/preps/image{}.png".format(i+ iOffset),"png")



args = ["inkscape", "Acaxochitlan.svg", 
		"--export-png=./acaxochitlan.png",
		"--export-area={}:{}:{}:{}".format(590,190, 640, 220),"-w=1280", "-h=720",
		"--export-background-opacity=255"]
	#print "save image", str(i)	
call(args)

args = ["inkscape", "Tenango.svg", 
		"--export-png=./tenango.png",
		"--export-area={}:{}:{}:{}".format(590,190, 640, 220),"-w=1280", "-h=720",
		"--export-background-opacity=255"]
	#print "save image", str(i)	
call(args)

args = ["inkscape", "Bartolo.svg", 
		"--export-png=./bartolo.png",
		"--export-area={}:{}:{}:{}".format(590,190, 640, 220),"-w=1280", "-h=720",
		"--export-background-opacity=255"]
	#print "save image", str(i)	
call(args)

args = ["inkscape", "Huehuetla.svg", 
		"--export-png=./huehuetla.png",
		"--export-area={}:{}:{}:{}".format(590,190, 640, 220),"-w=1280", "-h=720",
		"--export-background-opacity=255"]
	#print "save image", str(i)	
call(args)