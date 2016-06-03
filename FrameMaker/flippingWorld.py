import aggdraw
from PIL import Image
import math


class world:
    def __init__(self, start):
        self.startTime = start
        self.stopTime = start + 96
        self.world = Image.open("../Images/world.png")

    def draw(self, frame, image):
        if (frame < self.startTime or frame >= self.stopTime):
            return
        radius_x = 315
        radius_y = int(315 * (1 - math.sin(math.pi / 2. * ((frame - self.startTime) / 79.)))) if (
                                                                                                 frame - self.startTime) < 80 else 0
        offset_y = int(0.75 * (315 - radius_y))

        world = self.world.resize((2 * radius_x, 2 * radius_y), Image.BILINEAR)
        image.paste((0, 0, 0), (640 - radius_x, 360 - radius_y + offset_y), world)
        d = aggdraw.Draw(image)
        p = aggdraw.Pen("black", 8.46666)
        d.ellipse((640 - radius_x, 360 - radius_y + offset_y, 640 + radius_x, 360 + radius_y + offset_y), p)
        d.flush()
