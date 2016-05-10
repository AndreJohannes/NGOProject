from PIL import Image
import xml.etree.ElementTree as ET
from svg.path import parse_path
import aggdraw
import random
from Python.phrases import Phrases

im = Image.open("./images/preps/image199.png")

textMask = Phrases.getPhrase32(1000)
im.paste("black",(224, 445),textMask)
textMask = Phrases.getPhrase33(1000)
im.paste("black",(541, 127),textMask)
textMask = Phrases.getPhrase34(1000)
im.paste("black",(737, 426),textMask)
textMask = Phrases.getPhrase35(1000)
im.paste("black",(428, 462),textMask)
im.show()