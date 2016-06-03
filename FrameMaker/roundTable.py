import aggdraw
from PIL import Image

import Tools.helpers as Helpers
import Tools.transitions as Transitions
from Tools.frontender import evolve_base, languages
from Tools.phrases import Phrases


class still:
    def __init__(self, start):
        self.startTime = start
        self.stopTime = start + 265
        self.image = Image.open("./images/base15.png")

    def draw(self, frame, image):
        if (frame < self.startTime or frame >= self.stopTime):
            return
        image.paste(self.image, (0, 0))


class text:
    def __init__(self, start, duration, phrases, position, slow=None, color="black"):
        self.startTime = start
        self.stopTime = start + duration
        self.duration = duration
        self.phrases = phrases
        self.phrase = phrases[languages.ENGLISH]
        self.position = position
        self.slow = slow
        self.color = color

    def draw(self, frame, image):
        if (frame < self.startTime or frame >= self.stopTime):
            return
        idx = frame - self.startTime
        if self.slow == None:
            factor = self.phrase[1]
            textMask = self.phrase[0](int(idx * factor))
        else:
            textMask = self.phrase[0](idx if idx < self.slow else (idx - self.slow) / 4 + self.slow)
        image.paste(self.color, self.position, textMask)

    def set_language(self, language):
        ':type language: languages'
        if language == languages.ENGLISH:
            self.phrase = self.phrases[languages.ENGLISH]
        elif language == languages.SPANISH:
            self.phrase = self.phrases[languages.SPANISH]


class evolve(evolve_base):
    font = aggdraw.Font("white", "./fonts/calibrib.ttf", 46)
    text_english = [u"PSYDEH and Global Citizens:", u"growing trees with rural and", u"indigenous partners in Mexico."]
    text_spanish = [u"PSYDEH y Ciudadanos del Mundo:", u"tirando paredes y plantando arboles junto",
                    u"con nuestros socios ind\u00EDgenas en M\u00e9xico."]
    phrase1 = {languages.ENGLISH: [Phrases().makeImage_runnable(text_english, font, 50), 1.0],
               languages.SPANISH: [Phrases().makeImage_runnable(text_spanish, font, 50),
                                   Helpers.getLetterRatio(text_english, text_spanish)]}
    text_english = [u"Visit PSYDEH's website for more", u"information: "]
    text_spanish = [u"Para m\u00e1s informaci\u00f3n visita la", u"p\u00e1gina web de PSYDEH: "]
    phrase2 = {languages.ENGLISH: [Phrases().makeImage_runnable(text_english, font, 50), 1.0],
               languages.SPANISH: [Phrases().makeImage_runnable(text_spanish, font, 50),
                                   Helpers.getLetterRatio(text_english, text_spanish)]}

    text_english = [u"www.psydeh.com"]
    text_spanish = [u"www.psydeh.com"]
    phrase3 = {languages.ENGLISH: [Phrases().makeImage_runnable(text_english, font, 50), 1.0],
               languages.SPANISH: [Phrases().makeImage_runnable(text_spanish, font, 50),
                                   Helpers.getLetterRatio(text_english, text_spanish)]}

    def __init__(self, start):
        self.startTime = start
        self.stopTime = start + 265
        self.list = []
        self.list.append(still(start))
        self.list.append(text(start, 265, self.phrase1, (310, 50)))
        self.list.append(text(start + 85, 195, self.phrase2, (310, 600)))
        self.list.append(
            text(start + 85 + 44, 151, self.phrase3, (310 + 252 + 1 * 210, 600 + 50),
                 slow=0, color=(80, 147, 205)))
        self.list.append(Transitions.blender(None, Image.open("./images/base16_spanish.png"), start + 225, 40))
