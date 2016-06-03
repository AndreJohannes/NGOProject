from PIL import Image
from PIL import ImageDraw
from PIL import ImageOps
import aggdraw
import math
import random

for i in range(0, 43):
    base = Image.new("RGBA", (590, 590), (255, 255, 255, 0))
    image = ImageOps.invert(Image.open("frame{:02d}.png".format(i + 3)).convert("L"))
    base.paste("black", (2, 331), image)
    # base.show()
    base.save("../frame{}.png".format(i), "png")
