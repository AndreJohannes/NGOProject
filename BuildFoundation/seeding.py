from PIL import Image
from PIL import ImageOps
import aggdraw
import math

guy = ImageOps.invert(Image.open("./images/seeding/preps/right_guy.png")).convert("L")

for i in range(0, 34):
    image = Image.open("./images/seeding/preps/image{:02d}.png".format(i))
    image.paste("black", (0, 0), guy)

    image.save("./images/seeding/image{}.png".format(i), "png")
