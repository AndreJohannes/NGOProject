import math
import random


class perspective:
    def project(self, position, zoom):
        [x, y, z] = position
        C = 1000.
        return [640 + zoom * x * C / (C + z), 460 + zoom * y * C / (C + z)]

    def rotX(self, rad, position):
        [x, y, z] = position
        cos = math.cos(rad)
        sin = math.sin(rad)
        return [x, y * cos - z * sin, z * cos + y * sin]

    def rotY(self, rad, position):
        [x, y, z] = position
        cos = math.cos(rad)
        sin = math.sin(rad)
        return [cos * x - sin * z, y, cos * z + sin * x]
