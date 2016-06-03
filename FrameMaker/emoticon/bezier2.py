import bezier
import random
import math
from PIL import Image
import sys

# sys.path.append('../Tools')
# import frontender  # @UnresolvedImport

p1 = [715, 584]
p2 = [976, 557]
p3 = [1010, 305]


class evlove:
    def __init__(self, start):
        self.startTime = start
        self.stopTime = start + 100
        bez1 = bezier.specialBezier([[787 - 95, 489], [819 - 95, 465], [1060 - 95 + 100, 355 + 100]], 0.2)
        bez2 = bezier.specialBezier([[972 - 95, 646], [966 - 95, 667], [976 - 95, 607]], 1.0)
        coords1 = bez1.get_coordinates(25)
        print coords1
        coords2 = bez2.get_coordinates(25)
        coords = zip(coords1, coords2)
        coords_right = [[[coord[0][0] + random.randint(-2, 2), coord[0][1] + random.randint(-2, 2)],
                         [coord[1][0] + random.randint(-2, 2), coord[1][1] + random.randint(-2, 2)]] for coord in
                        coords]
        bez1 = bezier.specialBezier([[684 - 95, 750], [630 - 95, 663], [420 - 95 - 150, 355 + 100]], 1.0)
        bez2 = bezier.specialBezier([[501 - 95, 652], [481 - 95, 667], [454 - 95, 607]], 1.0)
        coords1 = bez1.get_coordinates(25)
        coords2 = bez2.get_coordinates(25)
        coords = zip(coords1, coords2)
        coords_left = [[[coord[0][0] + random.randint(-2, 2), coord[0][1] + random.randint(-2, 2)],
                        [coord[1][0] + random.randint(-2, 2), coord[1][1] + random.randint(-2, 2)]] for coord in coords]

        coords = zip(coords_right, coords_left)
        last = coords.pop()
        for i in range(1, 30):
            coords.append(last)
        self.coords = coords
        self.hand_left = bezier.hand()
        self.hand_right = bezier.hand(True)

    def draw(self, frame, image):
        image.paste(Image.open("./emoticon/test1.png"), (-95, 0))
        coord = self.coords[min((frame - self.startTime) / 3, 30)]
        bez = bezier.specialBezier([[715 - 95, 584], coord[0][1], coord[0][0]])
        bez.draw(image)
        points = bez.get_points()
        rad = math.atan2(points[2][0] - points[4][0], points[2][1] - points[4][1])
        self.hand_left.draw(image, (int(points[2][0]), int(points[2][1])), 90 + rad / math.pi * 180)
        bez = bezier.specialBezier([[715 - 95, 584], coord[1][1], coord[1][0]])
        bez.draw(image)
        points = bez.get_points()
        rad = math.atan2(points[2][0] - points[4][0], points[2][1] - points[4][1])
        self.hand_right.draw(image, (int(points[2][0]), int(points[2][1])), (-90 + rad / math.pi * 180))

        # class module:
        #    evolve = init

        # frontender.flicker([module])
