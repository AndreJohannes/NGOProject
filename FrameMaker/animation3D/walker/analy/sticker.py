from PIL import Image
from PIL import ImageDraw
import aggdraw
import math
import random


class stickman:
    def __init__(self, pos_crotch, orientation_leg1, orientation_lower_leg1, orientation_leg2, orientation_lower_leg2,
                 orientation_arm1, orientation_lower_arm1, orientation_arm2, orientation_lower_arm2):
        self.position = pos_crotch
        self.length_torso = 60
        self.length_leg = 50
        self.length_arm = 40
        self.radius_head = 35 / 2.
        self.orientation_torso = 0
        self.orientation_leg1 = orientation_leg1
        self.orientation_lower_leg1 = orientation_lower_leg1
        self.orientation_leg2 = orientation_leg2
        self.orientation_lower_leg2 = orientation_lower_leg2
        self.orientation_arm1 = orientation_arm1
        self.orientation_lower_arm1 = orientation_lower_arm1
        self.orientation_arm2 = orientation_arm2
        self.orientation_lower_arm2 = orientation_lower_arm2
        self.orientation_head = 0
        self.calculate_points()

    @staticmethod
    def getOrientation(pos1, pos2):
        return math.atan2(pos2[0] - pos1[0], -pos2[1] + pos1[1])

    @staticmethod
    def weightedAverageOrientation(ort1, ort2, w):
        return math.atan2((1 - w) * math.sin(ort1) + w * math.sin(ort2), (1 - w) * math.cos(ort1) + w * math.cos(ort2))

    @classmethod
    def fromPoints(cls, dict, offset):
        orientation_leg1 = cls.getOrientation(dict["crotch"], dict["knee_1"])
        orientation_leg2 = cls.getOrientation(dict["crotch"], dict["knee_2"])
        orientation_lower_leg1 = cls.getOrientation(dict["knee_1"], dict["foot_1"])
        orientation_lower_leg2 = cls.getOrientation(dict["knee_2"], dict["foot_2"])
        orientation_arm1 = cls.getOrientation(dict["neck"], dict["elbow_1"])
        orientation_arm2 = cls.getOrientation(dict["neck"], dict["elbow_2"])
        orientation_lower_arm1 = cls.getOrientation(dict["elbow_1"], dict["hand_1"])
        orientation_lower_arm2 = cls.getOrientation(dict["elbow_2"], dict["hand_2"])
        return cls((dict["crotch"][0] + offset[0], dict["crotch"][1] + offset[1]), orientation_leg1,
                   orientation_lower_leg1, orientation_leg2, orientation_lower_leg2,
                   orientation_arm1, orientation_lower_arm1, orientation_arm2, orientation_lower_arm2)

    @classmethod
    def getWeightedAverage(cls, stckman1, stckman2, w):
        orientation_leg1 = cls.weightedAverageOrientation(stckman1.orientation_leg1, stckman2.orientation_leg1, w)
        orientation_leg2 = cls.weightedAverageOrientation(stckman1.orientation_leg2, stckman2.orientation_leg2, w)
        orientation_lower_leg1 = cls.weightedAverageOrientation(stckman1.orientation_lower_leg1,
                                                                stckman2.orientation_lower_leg1, w)
        orientation_lower_leg2 = cls.weightedAverageOrientation(stckman1.orientation_lower_leg2,
                                                                stckman2.orientation_lower_leg2, w)
        orientation_arm1 = cls.weightedAverageOrientation(stckman1.orientation_arm1, stckman2.orientation_arm1, w)
        orientation_arm2 = cls.weightedAverageOrientation(stckman1.orientation_arm2, stckman2.orientation_arm2, w)
        orientation_lower_arm1 = cls.weightedAverageOrientation(stckman1.orientation_lower_arm1,
                                                                stckman2.orientation_lower_arm1, w)
        orientation_lower_arm2 = cls.weightedAverageOrientation(stckman1.orientation_lower_arm2,
                                                                stckman2.orientation_lower_arm2, w)
        return cls(((1 - w) * stckman1.position[0] + w * stckman2.position[0],
                    (1 - w) * stckman1.position[1] + w * stckman2.position[1]), orientation_leg1,
                   orientation_lower_leg1, orientation_leg2, orientation_lower_leg2,
                   orientation_arm1, orientation_lower_arm1, orientation_arm2, orientation_lower_arm2)

    def draw(self, image):
        canvas = aggdraw.Draw(image)
        pen = aggdraw.Pen("black", 7)
        brush = aggdraw.Brush("back", 255)
        canvas.line(self.x1 + self.x2, pen)
        canvas.line(self.x1 + self.x3, pen)
        canvas.line(self.x3 + self.x4, pen)
        canvas.line(self.x1 + self.x5, pen)
        canvas.line(self.x5 + self.x6, pen)
        canvas.line(self.x2 + self.x8, pen)
        canvas.line(self.x8 + self.x9, pen)
        canvas.line(self.x2 + self.x10, pen)
        canvas.line(self.x10 + self.x11, pen)
        r = self.radius_head
        canvas.ellipse((self.x7[0] - r, self.x7[1] - r, self.x7[0] + r, self.x7[1] + r), pen, None)
        canvas.ellipse((self.x1[0] - 3.5, self.x1[1] - 3.5, self.x1[0] + 3.5, self.x1[1] + 3.5), None, brush)
        canvas.ellipse((self.x3[0] - 3.5, self.x3[1] - 3.5, self.x3[0] + 3.5, self.x3[1] + 3.5), None, brush)
        canvas.ellipse((self.x4[0] - 3.5, self.x4[1] - 3.5, self.x4[0] + 3.5, self.x4[1] + 3.5), None, brush)
        canvas.ellipse((self.x5[0] - 3.5, self.x5[1] - 3.5, self.x5[0] + 3.5, self.x5[1] + 3.5), None, brush)
        canvas.ellipse((self.x6[0] - 3.5, self.x6[1] - 3.5, self.x6[0] + 3.5, self.x6[1] + 3.5), None, brush)
        canvas.ellipse((self.x8[0] - 3.5, self.x8[1] - 3.5, self.x8[0] + 3.5, self.x8[1] + 3.5), None, brush)
        canvas.ellipse((self.x9[0] - 3.5, self.x9[1] - 3.5, self.x9[0] + 3.5, self.x9[1] + 3.5), None, brush)
        canvas.ellipse((self.x10[0] - 3.5, self.x10[1] - 3.5, self.x10[0] + 3.5, self.x10[1] + 3.5), None, brush)
        canvas.ellipse((self.x11[0] - 3.5, self.x11[1] - 3.5, self.x11[0] + 3.5, self.x11[1] + 3.5), None, brush)
        canvas.flush()

    def calculate_points(self):
        self.x1 = self.position
        rad = self.orientation_torso
        self.x2 = (self.x1[0] + self.length_torso * math.sin(rad), self.x1[1] - self.length_torso * math.cos(rad))
        rad = self.orientation_leg1
        self.x3 = (self.x1[0] + self.length_leg * math.sin(rad), self.x1[1] - self.length_leg * math.cos(rad))
        rad = self.orientation_lower_leg1
        self.x4 = (self.x3[0] + self.length_leg * math.sin(rad), self.x3[1] - self.length_leg * math.cos(rad))
        rad = self.orientation_leg2
        self.x5 = (self.x1[0] + self.length_leg * math.sin(rad), self.x1[1] - self.length_leg * math.cos(rad))
        rad = self.orientation_lower_leg2
        self.x6 = (self.x5[0] + self.length_leg * math.sin(rad), self.x5[1] - self.length_leg * math.cos(rad))
        rad = self.orientation_head
        self.x7 = (self.x2[0] + self.radius_head * math.sin(rad), self.x2[1] - self.radius_head * math.cos(rad))
        rad = self.orientation_arm1
        self.x8 = (self.x2[0] + self.length_arm * math.sin(rad), self.x2[1] - self.length_arm * math.cos(rad))
        rad = self.orientation_lower_arm1
        self.x9 = (self.x8[0] + self.length_arm * math.sin(rad), self.x8[1] - self.length_arm * math.cos(rad))
        rad = self.orientation_arm2
        self.x10 = (self.x2[0] + self.length_arm * math.sin(rad), self.x2[1] - self.length_arm * math.cos(rad))
        rad = self.orientation_lower_arm2
        self.x11 = (self.x10[0] + self.length_arm * math.sin(rad), self.x10[1] - self.length_arm * math.cos(rad))


import pickle

frames = pickle.load(open("frames.p", "rb"))


def save(idx):
    if idx < 0 or idx > 107:
        return
    image.save("frame{}.png".format(idx), "png")


i = -6
d = 3 - 2 * 111
sm_old = None
for j in range(0, 5):
    for frame in frames:
        sm = stickman.fromPoints(frame, (d, 126))
        if sm_old != None:
            image = Image.new("RGBA", (590, 590))
            stickman.getWeightedAverage(sm_old, sm, 1 / 3.).draw(image)
            save(i)
            i += 1
            image = Image.new("RGBA", (590, 590))
            stickman.getWeightedAverage(sm_old, sm, 2 / 3.).draw(image)
            save(i)
            i += 1
        image = Image.new("RGBA", (590, 590))
        sm.draw(image)
        save(i)
        sm_old = sm
        i += 1
    d += 111
