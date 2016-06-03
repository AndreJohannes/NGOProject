from PIL import Image
from Tools.phrases import Phrases
import Tools.transitions as Transitions
import aggdraw
import math
import emoticon.bezier2 as bezier
from Tools.frontender import languages, evolve_base


class still:
    def __init__(self, start):
        self.startTime = start
        self.stopTime = start + 230
        self.image = Image.open("./images/base2.png")

    def draw(self, frame, image):
        if (frame < self.startTime or frame >= self.stopTime):
            return
        image.paste(self.image, (0, 0))


class bubble:
    def __init__(self, startTime):
        self.startTime = startTime

    def draw(self, frame, im):
        if frame < self.startTime:
            return
        # idx = frame - self.startTime
        radius_x = 600
        radius_y = 320
        pos_x = 640
        pos_y = 360
        canvas = aggdraw.Draw(im)
        pen = aggdraw.Pen("black", 3)
        brush = aggdraw.Brush((255, 255, 180), 230);
        path = aggdraw.Path()
        for grad in range(0, 360):
            dr = 20 * math.pow(math.sin(2 * grad / 180. * math.pi), 2)
            x = (dr + radius_x) * math.sin(grad / 180. * math.pi)
            y = (dr + radius_y) * math.cos(grad / 180. * math.pi)
            path.lineto(pos_x + x, pos_y + y)

        canvas.polygon(path.coords(), pen, brush)
        canvas.flush()


class text:
    def __init__(self, start, duration, fading, phrases):
        self.startTime = start
        self.stopTime = start + duration + fading
        self.duration = duration
        self.fading = fading
        self.phrases = phrases
        self.phrase = phrases[languages.ENGLISH]

    def draw(self, frame, image):
        if (frame < self.startTime or frame >= self.stopTime):
            return
        idx = frame - self.startTime
        if idx > self.duration:
            color = 255. * (1. - (idx - self.duration) / (self.fading - 1.))
            textMask = self.phrase(idx)
            textMask2 = Image.new("L", textMask.size, "black")
            textMask2.paste((color), (0, 0), textMask)
            image.paste("black", (620 - textMask2.size[0] / 2, int(165 - 0 * idx)), textMask2)
        else:
            textMask = self.phrase(idx)
            image.paste("black", (620 - textMask.size[0] / 2, int(165 - 0 * idx)), textMask)

    def set_language(self, language):
        ':type language: languages'
        if language == languages.ENGLISH:
            self.phrase = self.phrases[languages.ENGLISH]
        elif language == languages.SPANISH:
            self.phrase = self.phrases[languages.SPANISH]


class smile:
    def __init__(self):
        pass

    def draw(self, frame, image):
        im = Image.open("./emoticon/smile.png")
        image.paste("white", (620 - 0 * 95, 435, 810 - 0 * 95, 473))
        image.paste(im, (0 - 0 * 95, 0), im)


class evolve(evolve_base):
    font = aggdraw.Font(u"white", "./fonts/calibri.ttf", 46)
    text_english = [u"Join us in breaking down walls.", "             ",
                    u"Support these three initiatives.", "             ",
                    u"Help us grow our tree.", "             ",
                    u"Global citizens thrive in informed collaboration!"]
    text_spanish = [u"Acomp\u00e1\u00f1anos a tirar las paredes.", "             ",
                    u"Apoya estos tres proyectos.", "             ",
                    u"Ay\u00fadanos a que nuestro \u00e1rbol crezca.", "         ",
                    u"    \u00a1Los ciudadanos del mundo prosperan en colaboraci\u00f3n!"]

    phrase1 = {languages.ENGLISH: Phrases().makeImage_centered_runnable(text_english, font),
               languages.SPANISH: Phrases().makeImage_centered_runnable(text_spanish, font)}

    def __init__(self, start):
        self.startTime = start
        self.stopTime = start + 230
        self.list = []
        self.list.append(still(start))
        # self.list.append(bezier.evlove(start))
        self.list.append(smile())
        self.list.append(bubble(start))
        self.list.append(text(start, 180, 50, self.phrase1))
        self.list.append(Transitions.zapping(None, Image.open("./images/base15.png"), start + 210, 20))
