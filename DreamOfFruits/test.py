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

textMask = Phrases.getPhrase37(1000)
textMask.show()
#apple.paste("black",(30, 150),textMask)
#apple.show()