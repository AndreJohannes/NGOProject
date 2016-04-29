from subprocess import call

start = [0, 0, 1000, 680]
end = [530, 170, 660, 240]


for i in range(0,100):
	
	k = 1- i/99.

	x1 =k* start[0] + (1-k) *end[0]
	y1 =k* start[1] + (1-k) *end[1]
	x2 =k* start[2] + (1-k) *end[2]
	y2 =k* start[3] + (1-k) *end[3]

	args = ["inkscape", "Mexico_Map.svg", 
		"--export-png=./images/image{}.png".format(i),
		"--export-area={}:{}:{}:{}".format(x1,y1,x2,y2),"-w=1280", "-h=720"]

	call(args)

	



