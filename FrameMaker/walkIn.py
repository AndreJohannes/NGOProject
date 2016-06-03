from PIL import Image
from PIL import ImageDraw
import aggdraw
import math


class walk:
    def __init__(self, start):
        self.startTime = start
        self.stopTime = start + 96

    def draw(self, frame, image):
        if (frame < self.startTime or frame >= self.stopTime):
            return
        idx = (frame - self.startTime) / 2
        color = min((15 * idx), 256)
        im = Image.open("../WalkIn/images/walkin-" + str(min(idx, 37)) + ".png")
        im = im.convert("LA");
        im.paste((0, color), (0, 0, 1280, 720), im.convert("RGBA"))
        im_mirror = Image.open("../WalkIn/images/walkin-" + str(max(idx - 10, 0)) + ".png")
        im_mirror = im_mirror.transpose(Image.FLIP_LEFT_RIGHT)
        im_mirror = im_mirror.convert("LA")
        color = max(0, min((15 * (idx - 10)), 256))
        im_mirror.paste((0, color), (0, 0, 1280, 720), im_mirror.convert("RGBA"));
        image.paste((0, 0, 0, 256), (0, 0, 1280, 720), im.convert("RGBA"))
        image.paste((0, 0, 0, 256), (100, 0, 1380, 720), im_mirror.convert("RGBA"))
