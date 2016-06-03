from PIL import Image, ImageDraw
from PIL import ImageOps
import aggdraw
from Tools.phrases import Phrases
import Tools.transitions as Transitions
import Tools.helpers as Helpers
from Tools.frontender import evolve_base, languages


class image:
    def __init__(self, start, duration, image):
        self.startTime = start
        self.stopTime = start + duration
        self.duration = duration
        self.image = image

    def draw(self, frame, image):
        if (frame < self.startTime or frame >= self.stopTime):
            return
        image.paste(self.image, (0, 0))


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
            image.paste("black", (65, int(300 - 1.5 * idx * factor)), textMask2)
        else:
            factor = self.phrase[1]
            textMask = self.phrase[0](int(idx * factor))
            image.paste("black", (65, int(300 - 1.5 * idx * factor)), textMask)

    def set_language(self, language):
        ':type language: languages'
        if language == languages.ENGLISH:
            self.phrase = self.phrases[languages.ENGLISH]
        elif language == languages.SPANISH:
            self.phrase = self.phrases[languages.SPANISH]


class pullWall:
    def __init__(self, start):
        self.startTime = start
        self.stopTime = start + 360

    def draw(self, frame, image):
        if (frame < self.startTime or frame >= self.stopTime):
            return
        idx = frame - self.startTime
        im = Image.open(
            "../BuildFoundation/images/pullWall/image{:03d}.png".format(max(0, min(135, int((idx - 120) / 2.)))))
        d = aggdraw.Draw(im)
        p = aggdraw.Pen("black", 8.46666)
        d.ellipse((640 - 315, 596, 640 + 315, 596), p)
        d.flush()
        im = im.convert("L")
        im = ImageOps.invert(im)
        color = max(190 - 5 * max(0, idx - 120), 0)
        image.paste((color, color, color), (0, 0), im)


class handShake:
    def __init__(self, start):
        self.startTime = start
        self.stopTime = start + 320

    def draw(self, frame, image):
        if (frame < self.startTime or frame >= self.stopTime):
            return
        idx = frame - self.startTime
        im = Image.open("../BuildFoundation/images/handshake/image{:02d}.png".format(min(int((idx) / 2), 15)))
        d = aggdraw.Draw(im)
        p = aggdraw.Pen("black", 8.46666)
        d.ellipse((640 - 315, 596, 640 + 315, 596), p)
        d.flush()
        im = im.convert("L")
        im = ImageOps.invert(im)
        color = min(5 * idx, 190)
        image.paste((color, color, color), (0, 0), im)


class gradient:
    def __init__(self, start):
        self.startTime = start
        self.mask = Image.new("L", (900, 200), 255)
        draw = ImageDraw.Draw(self.mask)
        for idx in range(0, 200):
            draw.line((0, idx, 900, idx), fill=int(255 * max(0, idx - 150) / 50.))

    def draw(self, frame, image):
        if self.startTime > frame:
            return
        idx = frame - self.startTime
        color = min(5 * idx, 190)
        if idx > 100:
            color = max(0, 190 - 5 * (idx - 100))
        im = Image.new("L", (900, 200), color)
        im.paste("black", (0, 0), self.mask)
        image.paste("white", (100, 210), im)


class evolve(evolve_base):
    font = aggdraw.Font("white", "./fonts/calibrib.ttf", 56)
    text_english = [u"For centuries, indigenous people are", u"separated by walls, dividing community from",
                    u"community and the Region from the world.", u"             ",
                    u"The majority of the Region's people earn less", u"than $96usd per month.", u"             ",
                    u"Less than 1% of homes possess a computer.", "             ",
                    #u"Communities rarely collaborate, municipalities", u"even less.", u"             ",
                    u"Women average three grades of schooling."]

    text_spanish = [u"La gente ind\u00edgena est\u00e1 separada.",
                    u"Se dividen comunidad de comunidad",
                    u"y la Regi\u00f3n del mundo.", u"             ",
                    u"La mayor\u00eda de la gente de la Regi\u00f3n", u"gana menos de $96 d\u00f3lares al mes.",
                    "             ",
                    u"Menos de 1% de los hogares poseen", u"una computadora.", "             ",
                    #u"Las comunidades raramente colaboran entre", u"ellas, los municipios todav\u00eda menos.",
                    #"             ",
                    u"Las mujeres promedian solo tres",u"a\u00f1os de escolaridad."]

    phrase1 = {languages.ENGLISH: [Phrases().makeImage_runnable(text_english, font, 60), 1.],
               languages.SPANISH: [Phrases().makeImage_runnable(text_spanish, font, 60),
                                   Helpers.getLetterRatio(text_english, text_spanish)]}

    text_english = [u"Since 2013, Nahua, Otom\u00ed and Tepehua citizens",
                    u"defy the walls and build their own bottom-up",
                    u"rights-based movement.", "             ",
                    u"In partnership with the Mexican NGO PSYDEH,", u"in 2014 and 2015, a network of 500+ indigenous",
                    u"women from 35+ communities planted", u"innovative seeds for their sustainable future."]

    text_spanish = [u"Desde 2013, las poblaciones Nahua, Otom\u00ed y",
                    u"Tepehua desaf\u00edan las paredes y construyen su",
                    u"propio movimiento social desde la base", u"piramidal con respecto a sus derechos humanos.",
                    "             ",
                    u"En colaboraci\u00f3n con la ONG mexicana PSYDEH,",
                    u"en 2014 y 2015, una red de m\u00e1s de 500 mujeres",
                    u"ind\u00edgenas de m\u00e1s de 35 comunidades plantaron",
                    u"semillas de innovaci\u00f3n para su propio futuro", u"sustentable."]

    phrase2 = {languages.ENGLISH: [Phrases().makeImage_runnable(text_english, font, 60), 1.],
               languages.SPANISH: [Phrases().makeImage_runnable(text_spanish, font, 60),
                                   Helpers.getLetterRatio(text_english, text_spanish)]}

    text_english = [u"These seeds = learning about: ", "             ",
                    u"   - shared problems", "             ",
                    u"   - clarity on solutions", "             ",
                    u"   - leader disciplines to implement solutions", "             ",
                    u"   - rights & laws on which solutions are based", "             ",
                    u"   - personal & communal autonomy"]

    text_spanish = [u"Estas semillas = aprender acerca de: ", "             ",
                    u"   - Problemas en com\u00fan", "             ",
                    u"   - Claridad en soluciones", "             ",
                    u"   - M\u00e9todos de liderazgo para implementar", u"     soluciones", "             ",
                    u"   - Derechos y leyes en los que se basan las", u"     soluciones", "             ",
                    u"   - Autonom\u00eda personal y colectiva"]

    phrase3 = {languages.ENGLISH: [Phrases().makeImage_runnable(text_english, font, 60), 1.],
               languages.SPANISH: [Phrases().makeImage_runnable(text_spanish, font, 60),
                                   Helpers.getLetterRatio(text_english, text_spanish)]}

    def __init__(self, start):
        self.startTime = start
        self.stopTime = start + 1170
        self.list = []
        self.list.append(image(start, 470, Helpers.open_image("./images/base4.png", 190)))
        self.list.append(text(start, 420, 50, self.phrase1))
        self.list.append(pullWall(start + 470))
        self.list.append(gradient(start + 470 + 120))
        self.list.append(text(start + 470, 310, 50, self.phrase2))
        self.list.append(handShake(start + 830))
        self.list.append(text(start + 830, 270, 50, self.phrase3))
        self.list.append(Transitions.horizontalFlip(Helpers.open_image("./images/base5.png", 190).convert("RGBA"),
                                                    Image.open("./images/base6.png").convert("RGBA"), start + 1150, 20))
