from PIL import Image
import xml.etree.ElementTree as ET
from svg.path import parse_path
import aggdraw
import random
from Python.phrases import Phrases

for i in range(0, 300):

    flash = Image.open("./flash.png")
    im = Image.open("./images/preps/image{}.png".format(min(i, 199)))

    if i < 110:
        textMask = Phrases.getPhrase31(i)
        im.paste("black", (50, 320 - i), textMask)
    else:
        color = 255. * (1 - (i - 110) / 99.)
        textMask = Phrases.getPhrase31(1000)
        textMask2 = Image.new("L", textMask.size, "black")
        textMask2.paste((color), (0, 0), textMask)
        im.paste("black", (50, 320 - i), textMask2)

    textMask = Phrases.getPhrase34(max(0, (i - 130) / 2))
    im.paste("black" if i <= 210 else "white", (737, 426), textMask)
    if (i > 200 and i <= 210):
        sz = 100 * (i - 200)
        flash_rsz = flash.resize((sz, sz), Image.ANTIALIAS)
        im.paste((255, 255, 180), (793 - sz / 2, 454 - sz / 2), flash_rsz)

    textMask = Phrases.getPhrase35(max(0, (i - 140) / 2))
    im.paste("black" if i <= 234 else "white", (438, 462), textMask)
    if (i > 224 and i <= 234):
        sz = 100 * (i - 224)
        flash_rsz = flash.resize((sz, sz), Image.ANTIALIAS)
        im.paste((255, 255, 180), (495 - sz / 2, 492 - sz / 2), flash_rsz)

    textMask = Phrases.getPhrase33(max(0, (i - 160) / 2))
    im.paste("black" if i <= 228 else "white", (491, 123), textMask)
    if (i > 218 and i <= 228):
        sz = 100 * (i - 218)
        flash_rsz = flash.resize((sz, sz), Image.ANTIALIAS)
        im.paste((255, 255, 180), (603 - sz / 2, 157 - sz / 2), flash_rsz)

    textMask = Phrases.getPhrase32(max(0, (i - 180) / 2))
    im.paste("black" if i <= 279 else "white", (184, 415), textMask)
    if (i > 269 and i <= 279):
        sz = 100 * (i - 269)
        flash_rsz = flash.resize((sz, sz), Image.ANTIALIAS)
        im.paste((255, 255, 180), (295 - sz / 2, 477 - sz / 2), flash_rsz)

    im.save("./images/image{}.png".format(i), "png")
