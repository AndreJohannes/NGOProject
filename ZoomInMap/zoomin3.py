from PIL import Image
from PIL import ImageDraw
import aggdraw
from Python.phrases import Phrases
import Python.tools as Tools
import Python.transitions as Transitions

istart = 390

production = not False
iOffset = 1640 + istart if production else istart

dOffset = 70
for i in range(0, dOffset):
    im = Image.open("./images/preps/image{}.png".format(i + istart))

    textMask = Phrases.getPhrase25(i)
    im.paste("black", (50, 330), textMask)

    d = ImageDraw.Draw(im)
    d.text((0, 0), str(i + iOffset), "black")
    print "saving image:", i + iOffset
    im.save("./images/image" + str(i + iOffset) + ".png", "png") if not production else im.save(
        "../Movie/images/image" + str(i + iOffset) + ".png", "png")

iOffset += dOffset

ref = iOffset

dOffset = 40


def callback(im, i):
    color = 255 * (1 - min((i + iOffset - ref) / 20., 1.))
    textMask = Phrases.getPhrase25(1000)
    textMask2 = Image.new("L", textMask.size, "black")
    textMask2.paste((color), (0, 0), textMask)
    im.paste("black", (50, 330), textMask2)
    d = ImageDraw.Draw(im)
    d.text((0, 0), str(i + iOffset), "black")
    print "saving image:", i + iOffset
    im.save("./images/image" + str(i + iOffset) + ".png", "png") if not production else im.save(
        "../Movie/images/image" + str(i + iOffset) + ".png", "png")


Transitions.blender(Image.open("./otomi_close.png").convert("RGBA"),
                    Image.open("./acaxochitlan.png").convert("RGBA"), dOffset, callback)
iOffset += dOffset
Transitions.blender(Image.open("./acaxochitlan.png").convert("RGBA"),
                    Image.open("./tenango.png").convert("RGBA"), dOffset, callback)
iOffset += dOffset
Transitions.blender(Image.open("./tenango.png").convert("RGBA"),
                    Image.open("./bartolo.png").convert("RGBA"), dOffset, callback)
iOffset += dOffset
Transitions.blender(Image.open("./bartolo.png").convert("RGBA"),
                    Image.open("./huehuetla.png").convert("RGBA"), dOffset, callback)
iOffset += dOffset
Transitions.blender(Image.open("./huehuetla.png").convert("RGBA"),
                    Image.new("RGBA", (1280, 720), "white"), 20, callback)
