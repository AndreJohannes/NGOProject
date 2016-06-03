from PIL import Image
import aggdraw
from Tools.phrases import Phrases
import Tools.transitions as Transitions
import Tools.helpers as Helpers
from Tools.frontender import evolve_base, languages


class zoom:
    def __init__(self, start, phrases):
        self.startTime = start
        self.stopTime = start + 240
        self.phrases = phrases
        self.phrase = phrases[languages.ENGLISH]

    def draw(self, frame, image):
        if (frame < self.startTime or frame >= self.stopTime):
            return
        idx = frame - self.startTime
        image.paste(Image.open("../ZoomInMap/images/preps/image{}.png".format(min(idx, 169))), (0, 0))
        if idx >= 170:
            color = 255. * (1 - (idx - 170) / 69.)
            factor = self.phrase[1]
            textMask = self.phrase[0](int(idx * factor))
            textMask2 = Image.new("L", textMask.size, "black")
            textMask2.paste((color), (0, 0), textMask)
            image.paste("black", (50, 265), textMask2)
        else:
            factor = self.phrase[1]
            textMask = self.phrase[0](int(idx * factor))
            image.paste("black", (50, 265), textMask)

    def set_language(self, language):
        ':type language: languages'
        self.phrase = self.phrases[language]


class zoom2:
    def __init__(self, start):
        self.startTime = start
        self.stopTime = start + 70

    def draw(self, frame, image):
        if (frame < self.startTime or frame >= self.stopTime):
            return
        idx = frame - self.startTime
        image.paste(Image.open("../ZoomInMap/images/preps/image{}.png".format(min(idx + 390, 459))), (0, 0))


class regions:
    def __init__(self, start):
        self.startTime = start
        self.stopTime = start + 150
        self.blenders = []
        hidalgo = Image.open("./images/hidalgo.png")
        mezquital = Image.open("./images/mezquital.png")
        huasteca = Image.open("./images/huasteca.png")
        otomi = Image.open("./images/otomi.png")
        self.blenders.append(Transitions.blender(hidalgo, mezquital, start, 25))
        self.blenders.append(Transitions.blender(mezquital, huasteca, start + 25, 25))
        self.blenders.append(Transitions.blender(huasteca, otomi, start + 50, 25))

    def draw(self, frame, image):
        if (frame < self.startTime or frame >= self.stopTime):
            return
        for blender in self.blenders:
            blender.draw(frame, image)


class areas:
    def __init__(self, start):
        self.startTime = start
        self.stopTime = start + 160
        self.blenders = []
        otomi = Image.open("./images/otomi_close.png")
        acaxochitlan = Image.open("./images/acaxochitlan.png")
        tenango = Image.open("./images/tenango.png")
        bartolo = Image.open("./images/bartolo.png")
        huehuetla = Image.open("./images/huehuetla.png")
        self.blenders.append(Transitions.blender(otomi, acaxochitlan, start, 40))
        self.blenders.append(Transitions.blender(acaxochitlan, tenango, start + 40, 40))
        self.blenders.append(Transitions.blender(tenango, bartolo, start + 80, 40))
        self.blenders.append(Transitions.blender(bartolo, huehuetla, start + 120, 40))

    def draw(self, frame, image):
        if (frame < self.startTime or frame >= self.stopTime):
            return
        for blender in self.blenders:
            blender.draw(frame, image)


class text2:
    def __init__(self, start, phrases):
        self.startTime = start
        self.stopTime = start + 90
        self.phrases = phrases
        self.phrase = phrases[languages.ENGLISH]

    def draw(self, frame, image):
        if (frame < self.startTime or frame >= self.stopTime):
            return
        idx = frame - self.startTime
        if idx >= 70:
            color = 255. * (1 - (idx - 70) / 20.)
            factor = self.phrase[1]
            textMask = self.phrase[0](int(idx * factor))
            textMask2 = Image.new("L", textMask.size, "black")
            textMask2.paste((color), (0, 0), textMask)
            image.paste("black", (50, 290), textMask2)
        else:
            factor = self.phrase[1]
            textMask = self.phrase[0](int(idx * factor))
            image.paste("black", (50, 290), textMask)

    def set_language(self, language):
        ':type language: languages'
        self.phrase = self.phrases[language]


class evolve(evolve_base):
    font = aggdraw.Font("white", "./fonts/calibrib.ttf", 56)
    text_english = [u"Hidalgo is a small, ruggedly beautiful state in",
                    u"central Mexico where its indigenous citizens live",
                    u"in three regions in which human development",
                    u"levels are near the lowest in the world:"]
    text_spanish = [u"Hidalgo es un peque\u00f1o, rocoso y bello estado en",
                    u"M\u00e9xico central donde su poblacion indigena vive",
                    u"en tres regiones en las cuales el desarrollo humano",
                    u"se encuentra cerca de los m\u00e1s bajos del mundo:"]
    text_german = [u"Hidalgo ist ein kleiner, zerkl\u00fcfteter und pittoresker",
                   u"Bundesstatt im Herzen Mexikos in dem seine",
                   u"einheimische Bevoelkerung in drei Region lebt in",
                   u"denen die humane Entwicklung mit am niedrigsten",
                   u"in der Welt ist:"]

    phrase1 = {languages.ENGLISH: [Phrases().makeImage_runnable(text_english, font, 60), 1.0],
               languages.SPANISH: [Phrases().makeImage_runnable(text_spanish, font, 60),
                                   Helpers.getLetterRatio(text_english, text_spanish)],
               languages.GERMAN: [Phrases().makeImage_runnable(text_german, font, 60),
                                  Helpers.getLetterRatio(text_english, text_german)]}

    text_english = [u"In the Otom\u00ed-Tepehua region sit four majority",
                    u"indigenous areas:"]
    text_spanish = [u"En la regi\u00f3n Otom\u00ed-Tepehua hay cuatro \u00e1reas",
                    u"mayoritariamente ind\u00edgenas:"]
    text_german = [u"In der Region Otomi-Tepehua befinden sich 4",
                   u"mehrheitlich indigene Gebiete:"]

    phrase2 = {languages.ENGLISH: [Phrases().makeImage_runnable(text_english, font, 60), 1.0],
               languages.SPANISH: [Phrases().makeImage_runnable(text_spanish, font, 60),
                                   Helpers.getLetterRatio(text_english, text_spanish)],
               languages.GERMAN: [Phrases().makeImage_runnable(text_german, font, 60),
                                  Helpers.getLetterRatio(text_english, text_german)]}

    def __init__(self, start):
        self.startTime = start
        self.stopTime = start + 585
        self.list = [zoom(start, self.phrase1)]
        self.list.append(regions(start + 240))
        self.list.append(zoom2(start + 315))
        self.list.append(areas(start + 385))
        self.list.append(text2(start + 315, self.phrase2))
        self.list.append(
            Transitions.blender(Image.open("./images/huehuetla.png"), Helpers.open_image("./images/base4.png", 190),
                                start + 545, 40))
