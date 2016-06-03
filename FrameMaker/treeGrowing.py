import aggdraw
from PIL import Image

import Tools.helpers as Helpers
import Tools.transitions as Transitions
from Tools.frontender import languages, evolve_base
from Tools.phrases import Phrases


class seeding:
    def __init__(self, start):
        self.startTime = start
        self.stopTime = start + 50

    def draw(self, frame, image):
        if (frame < self.startTime or frame >= self.stopTime):
            return
        idx = frame - self.startTime
        im = Image.open("../BuildFoundation/images/seeding/image{}.png".format(min(idx, 33)))
        image.paste(im, (0, 46))


class watering:
    def __init__(self, start):
        self.startTime = start
        self.stopTime = start + 50

    def draw(self, frame, image):
        if (frame < self.startTime or frame >= self.stopTime):
            return
        idx = frame - self.startTime
        im = Image.open("../BuildFoundation/images/watering/image{:02d}.png".format(min(idx, 41)))
        image.paste(im, (0, 46))


class growing:
    def __init__(self, start):
        self.startTime = start
        self.stopTime = start + 300

    def draw(self, frame, image):
        if (frame < self.startTime or frame >= self.stopTime):
            return
        idx = frame - self.startTime
        im = Image.open("../BuildTree/images/image{}.png".format(min(int(1.5 * idx - idx * idx / 980.), 199)))
        if idx > 120:
            mask = Image.new("L", (1280, 720), max(255 - (idx - 120), 165))
            image.paste(im, (0, 0), mask)
        else:
            image.paste(im, (0, 0))


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
            factor = self.phrase[1]
            textMask = self.phrase[0](int(idx * factor))
            textMask2 = Image.new("L", textMask.size, "black")
            textMask2.paste((color), (0, 0), textMask)
            image.paste("black", (65, 300 - idx), textMask2)
        else:
            factor = self.phrase[1]
            textMask = self.phrase[0](int(idx * factor))
            image.paste("black", (65, 300 - idx), textMask)

    def set_language(self, language):
        ':type language: languages'
        if language == languages.ENGLISH:
            self.phrase = self.phrases[languages.ENGLISH]
        elif language == languages.SPANISH:
            self.phrase = self.phrases[languages.SPANISH]


class evolve(evolve_base):
    font = aggdraw.Font("white", "./fonts/calibrib.ttf", 56)

    text_english = [u"Where walls once existed, seeds are planted",
                    u"and a tree grows."]
    text_spanish = [u"En donde las paredes alguna vez existieron,",
                    u"las semillas se plantan y un \u00e1rbol crece."]

    phrase1 = {languages.ENGLISH: [Phrases().makeImage_runnable(text_english, font, 60), 1.0],
               languages.SPANISH: [Phrases().makeImage_runnable(text_spanish, font, 60),
                                   Helpers.getLetterRatio(text_english, text_spanish)]}

    text_english = [u"This tree, our", u"metaphor for", u"sustainability,", u"symbolizes our", u"work."]
    text_spanish = [u"Este \u00e1rbol,",u"simboliza nuestro",u"trabajo y nuestra",
                    u"met\u00e1fora de", u"sustentabilidad.",
                    ]

    phrase2 = {languages.ENGLISH: [Phrases().makeImage_runnable(text_english, font, 60), 1.0],
               languages.SPANISH: [Phrases().makeImage_runnable(text_spanish, font, 60),
                                   Helpers.getLetterRatio(text_english, text_spanish)]}

    def __init__(self, start):
        self.startTime = start
        self.stopTime = start + 340
        self.list = []
        self.list.append(seeding(start))
        self.list.append(watering(start + 50))
        self.list.append(growing(start + 100))
        self.list.append(text(start + 80, 70, 50, self.phrase1))
        self.list.append(text(start + 200, 70, 50, self.phrase2))
        self.list.append(
            Transitions.pageFlip(Image.open("./images/base7.png"), Image.open("./images/base10.png").convert("RGBA"),
                                 start + 320, 20))
