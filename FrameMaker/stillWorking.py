from PIL import Image
import aggdraw
from Tools.phrases import Phrases
import Tools.helpers as Helpers
from Tools.frontender import languages, evolve_base


class labour:
    def __init__(self, start):
        self.startTime = start
        self.stopTime = start + 100

    def draw(self, frame, image):
        if (frame < self.startTime or frame >= self.stopTime):
            return
        idx = frame - self.startTime
        im = Image.open("../WorkOnFoundation/images/image{}.png".format(idx))
        image.paste(im, (0, 0))


class slider:
    def __init__(self, start):
        self.startTime = start
        self.stopTime = start + 100

    def draw(self, frame, image):
        if (frame < self.startTime or frame >= self.stopTime):
            return
        idx = frame - self.startTime
        base = Image.open("../WorkOnFoundation/images/image{}.png".format(idx + 100))
        im = Image.open("../Pensombre/images/slider/image{:02d}.png".format(25 - idx)).convert("RGBA")
        dic = {10: 1221, 11: 1196, 12: 1153, 13: 1096, 14: 1022, 15: 952, 16: 874, 17: 797, 18: 724, 19: 646, 20: 562,
               21: 476, 22: 391, 23: 297, 24: 208, 25: 80}
        if (dic.has_key(25 - idx)):
            mask = Image.new("L", (1280, 720), "white")
            mask.paste("black", (0, 0, dic[25 - idx], 720))
            im.paste(base, (0, 0), mask)
        image.paste(im, (0, 0))


class text:
    def __init__(self, start, phrases):
        self.startTime = start
        self.stopTime = start + 125
        self.phrases = phrases
        self.lanaguage = languages.ENGLISH
        self.phrase = phrases[languages.ENGLISH]

    def draw(self, frame, image):
        if (frame < self.startTime or frame >= self.stopTime):
            return
        idx = frame - self.startTime
        if idx > 100:
            color = 255. * (1. - (idx - 100) / (25.))
            factor = self.phrase[1]
            textMask = self.phrase[0](int(idx * factor))
            textMask2 = Image.new("L", textMask.size, "black")
            textMask2.paste((color), (0, 0), textMask)
            image.paste("black", (65, 300 - idx*(2 if self.lanaguage==languages.SPANISH else 1)), textMask2)
        else:
            factor = self.phrase[1]
            textMask = self.phrase[0](int(idx * factor))
            image.paste("black", (65, 300 - idx*(2 if self.lanaguage==languages.SPANISH else 1)), textMask)

    def set_language(self, language):
        ':type language: languages'
        self.lanaguage = language
        if language == languages.ENGLISH:
            self.phrase = self.phrases[languages.ENGLISH]
        elif language == languages.SPANISH:
            self.phrase = self.phrases[languages.SPANISH]


class evolve(evolve_base):
    font = aggdraw.Font("white", "./fonts/calibrib.ttf", 56)
    text_english = [u"Still, as of May", u"2016, our tree", u"is not strong", u"enough to bear", u"fruit. The",
                    u"foundation", u"remains weak."]
    text_spanish = [u"Sin embargo,",u"hasta mayo del", u"2016, nuestro", u"\u00e1rbol no", u"ha sido lo",u"suficientemente", u"fuerte para",
                    u"brotar frutos.", u"La base a\u00fan es", u"d\u00e9bil."]

    phrase1 = {languages.ENGLISH: [Phrases().makeImage_runnable(text_english, font, 60), 1.0],
               languages.SPANISH: [Phrases().makeImage_runnable(text_spanish, font, 60),
                                   Helpers.getLetterRatio(text_english, text_spanish)]}

    def __init__(self, start):
        self.startTime = start
        self.stopTime = start + 125
        self.list = []
        self.list.append(labour(start))
        self.list.append(slider(start + 100))
        self.list.append(text(start, self.phrase1))
