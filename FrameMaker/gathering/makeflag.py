'''
Created on 26/05/2016

@author: andre
'''
import sys
sys.path
sys.path.append('../Tools')
import helpers  # @UnresolvedImport
import Image
import math
import random

class Flags:
    
    american = Image.open("../Flags/america.png").resize((910, 580), Image.ANTIALIAS)
    australia = Image.open("../Flags/australia.png").resize((910, 580), Image.ANTIALIAS)
    mexico = Image.open("../Flags/mexican.png").resize((910, 580), Image.ANTIALIAS)
    argentina = Image.open("../Flags/argentina.png").resize((910, 580), Image.ANTIALIAS)
    german = Image.open("../Flags/german.png").resize((910, 580), Image.ANTIALIAS)
    brazil = Image.open("../Flags/brazil.png").resize((910, 580), Image.ANTIALIAS)
    spain = Image.open("../Flags/spanish.png").resize((910, 580), Image.ANTIALIAS)
    japan = Image.open("../Flags/japan.png").resize((910, 580), Image.ANTIALIAS)

    list_of_flags = [american,
                     australia,
                     mexico,
                     argentina,
                     german,
                     brazil,
                     spain,
                     japan]


image = Image.new("RGBA", (1280, 720), "white")

offset_x = 150
offset_y = 150
for flag in Flags.list_of_flags:
    flag = flag.convert("RGBA")
    rad = random.randint(-10, 10) / 10.
    dz = 910 * math.sin(rad)
    C = 5000
    dx = 910 * math.cos(rad) * C / (C + dz)
    dy = 580 * C / (C + dz) 

    rec2 = [[0, 0], [flag.size[0], 0], [flag.size[0], flag.size[1]], [0, flag.size[1]]]
    if dy > 580:
        dyy = -(580 - dy) / 2
        rec1 = [[0, dyy], [dx, 0], [dx, dy], [0, 580 + dyy]]
    else:
        dyy = (580 - dy) / 2
        rec1 = [[0, 0], [dx, dyy], [dx, dy + dyy], [0, 580]]
    data = helpers.find_coeffs(rec1, rec2).tolist()
    tm = flag.transform((1000, 700), Image.PERSPECTIVE, data, Image.BICUBIC).resize((100, 70),
                                                                                    Image.ANTIALIAS)

    image.paste(tm, (offset_x, offset_y), tm)
    offset_x += 150
    if (offset_x > 1000):
        offset_x = 150
        offset_y += 150

image.show()
image.save("flags.png", "png")
