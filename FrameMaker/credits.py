from PIL import Image
from Tools.phrases import Phrases
import aggdraw
from Tools.frontender import languages, evolve_base


class still:
    def __init__(self, start):
        self.startTime = start
        self.stopTime = start + 200
        self.image = Image.open("./images/credits.png")

    def draw(self, frame, image):
        if (frame < self.startTime or frame >= self.stopTime):
            return
        image.paste(self.image, (0, 0))


class text:
    def __init__(self, start, duration, phrases, position):
        self.startTime = start
        self.stopTime = start + duration
        self.duration = duration
        self.phrases = phrases
        self.phrase = phrases[languages.ENGLISH]
        self.position = position

    def draw(self, frame, image):
        if (frame < self.startTime or frame >= self.stopTime):
            return
        textMask = self.phrase(1000)
        image.paste("white", (640 - textMask.size[0] / 2, self.position), textMask)

    def set_language(self, language):
        ':type language: languages'
        if language == languages.ENGLISH:
            self.phrase = self.phrases[languages.ENGLISH]
        elif language == languages.SPANISH:
            self.phrase = self.phrases[languages.SPANISH]


class evolve(evolve_base):
    font = aggdraw.Font("white", "./fonts/calibri.ttf", 46)
    text_english = [u"CITIZENS THRIVE IN COLLABORATION"]
    text_spanish = [u"CIUDADANOS PROPSERAN EN COLABORACI\u00d3N"]

    phrase1 = {languages.ENGLISH: Phrases().makeImage_centered_runnable(text_english, font),
               languages.SPANISH: Phrases().makeImage_centered_runnable(text_spanish, font)}

    font = aggdraw.Font("white", "./fonts/calibri.ttf", 26)
    text_english = [u"Background song \"Learn to Live With What You're Not\" by Steve",
                    u"Combs has been slightly edited and available for public sharing and",
                    u"adaptation from freemusicarchive.org under an Adaptation license."]
    text_spanish = [u"Canci\u00f3n en el fondo \"Learn to Live With What You're Not\" por Steve Combs ha sido",
                    u"ligeramente editada y est\u00e1 disponible para compartirse p\u00fablicamente y adaptada por",
                    u"Freemusicarchive.org bajo una Licencia de adaptacion."]

    phrase2 = {languages.ENGLISH: Phrases().makeImage_centered_runnable(text_english, font),
               languages.SPANISH: Phrases().makeImage_centered_runnable(text_spanish, font)}

    def __init__(self, start):
        self.startTime = start
        self.stopTime = start + 200
        self.list = []
        self.list.append(still(start))
        self.list.append(text(start, 200, self.phrase1, 460))
        self.list.append(text(start, 200, self.phrase2, 580))
