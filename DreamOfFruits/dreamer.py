from PIL import Image
import aggdraw
import random
from Python.phrases import Phrases
import math

base = Image.open("./images/preps/base.png")
lupa = Image.open("./images/preps/lupa.png")
mask = Image.open("./images/preps/mask.png").convert("L")
apple = Image.open("./images/preps/apple_big.png").resize((350,350),Image.ANTIALIAS)
size = 436 / 2
apple_dx = size-apple.size[0] / 2
apple_dy = size-apple.size[1] / 2


positions = [(400,237)]
positions.append((600,333))
positions.append((396,380))
positions.append((568,193))
positions.append((529,352))
positions.append((663,238))
positions.append((409,304))
positions.append((723,372))
positions.append((540,290))

textMasks  = [Phrases.getPhrase37(1000)]
textMasks.append(Phrases.getPhrase38(1000)) 
textMasks.append(Phrases.getPhrase39(1000))
textMasks.append(Phrases.getPhrase40(1000))
textMasks.append(Phrases.getPhrase41(1000))
textMasks.append(Phrases.getPhrase42(1000))
textMasks.append(Phrases.getPhrase43(1000))
textMasks.append(Phrases.getPhrase44(1000))
textMasks.append(Phrases.getPhrase45(1000))

iOffset = 0

for i in range(0,150):
	im = base.copy()
	textMask = Phrases.getPhrase36(i)
	im.paste("black",(775, 135),textMask)
	if i>100:
		sz = min(i-100,35)
		app = apple.resize((sz,sz),Image.ANTIALIAS)
		for position in positions:
			im.paste(app,position,app)
	im.save("./images/image{}.png".format(i+iOffset),"png")

iOffset += 150
position_old = (0,0)

for position in positions:

	for i in range(0, 50):
		k = math.pow(math.sin(math.pi /2. * i/49.),8)
		x = int((1-k) * position_old[0] + k*(position[0]))
		y = int((1-k) * position_old[1] + k*(position[1]))
		im2 = im.copy()
		area = base.crop((x-size/5,y-size/5,x+size/5,y+size/5))
		area = area.resize((size*2,2*size), Image.ANTIALIAS)
		c = 0
		for appl in positions:
			ax = appl[0]
			ay = appl[1] 
			pos=(apple_dx - 5*(x-ax),apple_dy - 5*(y-ay))
			awt = apple.copy()
			textMask = textMasks[c]
			awt.paste("black",(175-textMask.size[0]/2, 150),textMask)
			area.paste(awt,pos, apple)
			c += 1
		im2.paste(area,(x-size,y-size),mask)
		im2.paste(lupa,(x-254,y-244),lupa)
		im2.save("./images/image{}.png".format(i+iOffset),"png")

	position_old = position	
	iOffset += 50