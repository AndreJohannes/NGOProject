from PIL import Image
from PIL import ImageDraw
import aggdraw
import math

ioffset = 300

for i in range(0,48):
	base1 = Image.open("../BubbleWorld/images/image"+ str(ioffset+2*i) +".png")
	base2 = Image.open("../BubbleWorld/images/image"+ str(ioffset+2*i+1) +".png")
	#base1 =	base1.convert("LA")
	#base2 = base2.convert("LA")
	image = Image.open("./images/walkin-"+ str(min(i,37)) +".png")
	image = image.convert("LA");
	image_mirror = Image.open("./images/walkin-"+ str(max(i-10,0)) +".png")
	image_mirror = image_mirror.transpose(Image.FLIP_LEFT_RIGHT)
	image_mirror = image_mirror.convert("LA")
	color = min((15*i),256)
	image.paste((0,color),(0, 0, 1280, 720), image.convert("RGBA"))	

	base1.paste((0,0,0,256),(0, 0, 1280, 720), image.convert("RGBA"))
	base2.paste((0,0,0,256),(0, 0, 1280, 720), image.convert("RGBA"))
	color = max(0,min((15*(i-10)),256))
	image_mirror.paste((0,color),(0, 0, 1280, 720), image_mirror.convert("RGBA"));
	base1.paste((0,0,0,256),(100, 0, 1380, 720), image_mirror.convert("RGBA"))
	base2.paste((0,0,0,256),(100, 0, 1380, 720), image_mirror.convert("RGBA"))
	base1 = base1.convert("RGBA");
	base2 = base2.convert("RGBA");
	base1.save("../Movie/images/image" + str(ioffset+2*i) +".png")
	base2.save("../Movie/images/image" + str(ioffset+2*i+1) +".png")