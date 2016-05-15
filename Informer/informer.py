from PIL import Image
from PIL import ImageDraw
from PIL import ImageOps   
import aggdraw
from Python.phrases import Phrases
import Python.tools as Tools
import Python.transitions as Transitions

im = Image.open("./base.png")
im = im.convert("L")
im = ImageOps.invert(im)



production = not False
iOffset = 2280 if production else 0

for i in range(0, 470):

	color = max(255-i*6,190)
	base = Image.new("RGBA",(1280,720),"white")
	base.paste((color,color,color),(0,0),im)


	if (i>420):
		color = 255.*(1-(i-420)/49.)
		textMask = Phrases.getPhrase26(1000)
		textMask2 = Image.new("L",textMask.size,"black")
		textMask2.paste((color),(0,0),textMask)
		base.paste("black",(50, 300-i),textMask2)
	else:
		textMask = Phrases.getPhrase26(i)
		base.paste("black",(50, 300-i),textMask)

	d = ImageDraw.Draw(base)
	d.text((0,0),str(i+iOffset),"black")
	print "saving image:" , i + iOffset 
	base.save("./images/image" + str(i+iOffset) + ".png","png") if not production else base.save("../Movie/images/image" + str(i+iOffset) + ".png","png")

iOffset += 470
for i in range(0, 360):	
	
	im = Image.open("../BuildFoundation/images/pullWall/image{:03d}.png".format(max(0,min(135,int((i-120)/2.)))))
	d = aggdraw.Draw(im)
	p = aggdraw.Pen("black", 8.46666)
	d.ellipse((640-315,596,640+315,596),p)
	d.flush()
	im = im.convert("L")
	im = ImageOps.invert(im)
	color = max(190-5*max(0,i-120),0)
	base = Image.new("RGBA",(1280,720),"white")
	base.paste((color,color,color),(0,0),im)

	t1 = 310
	if 	(i>=t1):
		color = 255.*(1-(i-t1)/49.)
		textMask = Phrases.getPhrase27(1000)
		textMask2 = Image.new("L",textMask.size,"black")
		textMask2.paste((color),(0,0),textMask)
		base.paste("black",(50, 300-i),textMask2)
	else:
		textMask = Phrases.getPhrase27(i)
		base.paste("black",(50, 300-i),textMask)	

	d = ImageDraw.Draw(base)
	d.text((0,0),str(i+iOffset),"black")
	print "saving image:" , i + iOffset 
	base.save("./images/image" + str(i+iOffset) + ".png","png") if not production else base.save("../Movie/images/image" + str(i+iOffset) + ".png","png")

