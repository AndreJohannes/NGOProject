from PIL import Image
from Tools.phrases import Phrases
import Tools.transitions as Transitions
import aggdraw
import math


class still:
    
    def __init__(self, start):
        self.startTime = start
        self.stopTime = start + 200
        self.image = Image.open("./images/credits.png")
    
    def draw(self, frame, image):
        if(frame < self.startTime or frame >= self.stopTime):
            return
        image.paste(self.image, (0, 0))

class text:
    
    def __init__(self, start, duration, phrase, position):
        self.startTime = start
        self.stopTime = start + duration
        self.duration = duration
        self.phrase = phrase 
        self.position = position

    def draw(self, frame, image):
        if(frame < self.startTime or frame >= self.stopTime):
            return
        textMask = self.phrase(1000)
        image.paste("white", (640 - textMask.size[0] / 2, self.position), textMask)

class evolve:
    
    def __init__(self, start):
        self.startTime = start
        self.stopTime = start + 200
        self.list = []
        self.list.append(still(start))
        font1 = aggdraw.Font("white", "./fonts/calibri.ttf", 46)
        phrase1 = ["CITIZENS THRIVE IN COLLABORATION"]
        self.list.append(text(start, 200, Phrases().makeImage_centered_runnable(phrase1, font1), 460))
        font1 = aggdraw.Font("white", "./fonts/calibri.ttf", 26)
        phrase1 = ["Background song \"Learn to Live With What You're Not\" by Steve",
                    "Combs has been slightly edited and available for public sharing and",
                    "adaptation from freemusicarchive.org under an Adaptation license."]
        self.list.append(text(start, 200, Phrases().makeImage_centered_runnable(phrase1, font1), 580))


    def draw(self, frame, image):
        if(frame < self.startTime or frame >= self.stopTime):
            return
        for obj in self.list:
            obj.draw(frame, image)
        # if frame == self.startTime:
        #    image.save("./images/base16.png","png") 
