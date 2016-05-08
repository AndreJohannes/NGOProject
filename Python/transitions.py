from PIL import Image
from PIL import ImageDraw
import aggdraw
import math
import random
import Python.helpers as helpers

def blender(image1, image2, imax, callback):
	for i in range(0,imax):	
		color = (255. * i) / (imax-1)
		base = image1.copy()
		mask = Image.new("L",(1280,720),(color))
		#mask.paste("black",(0,0,dic[i-170],720))
		base.paste(image2,(0,0),mask)
		callback(base, i)

def zapping(image1, image2, imax, callback):
	for i in range(0,imax):	
		m = 10 * i  - 126
		base = image1.copy()
		mask = Image.new("L",(1280,720),"black")
		d = ImageDraw.Draw(mask)
		for x in range(0,1280):
			for y in range(0,720):
				d.point((x,y),random.randint(min(max(m-126,0),255),min(m+126,255)))
		#mask.paste("black",(0,0,dic[i-170],720))
		base.paste(image2,(0,0),mask)
		callback(base, i)

def pageflip(image1, image2, imax, callback):

	rect_right = [[640,0],[1280,0],[1280,720],[640,720]]
	rect_left = [[0,0],[640,0],[640,720],[0,720]]
	imax = imax/2

	for i in range(0,imax):

		om1 = Image.new("RGBA",(1280,720),"white")
		om2 = Image.new("RGBA",(1280,720),"white")

		rad = -i / (2.0*imax) * math.pi

 		dz  = 640 * math.sin(rad)
 		C = 2000
		dx = 640 * math.cos(rad) * C / (C+dz)
		dy = 360 * C / (C+dz) 

		pa = [[640, 0],[640+dx,360-dy],[640+dx,360+dy],[640,720]]
		data =  helpers.find_coeffs(pa,rect_right).tolist()
		tm = image1.transform((1280,720), Image.PERSPECTIVE,data,  Image.BICUBIC).crop((640,0,1280,720))

		rad = -i / (2.0*imax) * math.pi

 		dz  = 640 * math.sin(rad)
 		C = 2000
		dx = 640 * math.cos(rad) * C / (C+dz)
		dy = 360 * C / (C+dz) 

		pa = [[640-dx,360-dy],[640,0],[640,720],[640-dx,360+dy]]
		data =  helpers.find_coeffs(pa,rect_left).tolist()
		tm2 = image2.transform((1280,720), Image.PERSPECTIVE,data,  Image.BICUBIC).crop((0,0,640,720))

		om1.paste(image1.crop((0,0,640,720)),(0,0))
		om1.paste(image2.crop((640,0,1280,720)),(640,0))
		if i==0:
			om = om1.copy()
			d = aggdraw.Draw(om)
			p = aggdraw.Pen("black", 0.5)
			d.line((640, 0, 640, 720), p)
			d.flush()
			callback(om, imax)
	
		om2.paste(om1,(0,0))
		om1.paste(tm,(640,0),tm)
		d = aggdraw.Draw(om1)
		p = aggdraw.Pen("black", 0.5)
		d.line((640+dx, 0, 640+dx, 720), p)
		d.flush()
		om2.paste(tm2,(0,0),tm2)
		d = aggdraw.Draw(om2)
		p = aggdraw.Pen("black", 0.5)
		d.line((640-dx, 0, 640-dx, 720), p)
		d.flush()

		callback(om1, i)
		callback(om2, 2*imax - i )	

def horizontalflip(image1, image2, imax, callback):

	rect = [[0,0],[1280,0],[1280,720],[0,720]]
	imax = imax/2

	image1 = image1.convert("RGBA")
	image2 = image2.convert("RGBA")
	callback(Image.new("RGBA",(1280,720),"white"), imax)

	for i in range(0, imax):

		om1 = Image.new("RGBA",(1280,720),"white")
		om2 = Image.new("RGBA",(1280,720),"white")

		rad = -i / (2.0*imax) * math.pi
 		dz  = 360 * math.sin(rad)
 		C = 2000
		dx1 = 640  * C / (C-dz)
		dy1 = 360 * math.cos(rad) * C / (C-dz) 
		dx2 = 640  * C / (C+dz)
		dy2 = 360 * math.cos(rad) * C / (C+dz) 

		pa = [[640-dx1, 360-dy1],[640+dx1,360-dy1],[640+dx2,360+dy2],[640-dx2,360+dy2]]
		data =  helpers.find_coeffs(pa,rect).tolist()
		tm = image1.transform((1280,720), Image.PERSPECTIVE,data,  Image.BICUBIC)
		om1.paste(tm,(0,0), tm)
		callback(om1, i)

		pa = [[640-dx2, 360-dy2],[640+dx2,360-dy2],[640+dx1,360+dy1],[640-dx1,360+dy1]]
		data =  helpers.find_coeffs(pa,rect).tolist()
		tm2 = image2.transform((1280,720), Image.PERSPECTIVE,data,  Image.BICUBIC)
		om2.paste(tm2,(0,0), tm2)
		callback(om2 ,-i+2*imax)

