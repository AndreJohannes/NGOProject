from PIL import Image
import aggdraw
import math
from Tools.phrases import Phrases
import Tools.transitions as Transitions
from Tools.frontender import languages, evolve_base
import Tools.helpers as Helpers


class still:
    def __init__(self, start):
        self.startTime = start
        self.stopTime = start + 450
        self.image = Image.open("./images/base10.png")

    def draw(self, frame, image):
        if (frame < self.startTime or frame >= self.stopTime):
            return
        image.paste(self.image, (0, 0))


class text:
    def __init__(self, start, duration, phrases):
        self.startTime = start
        self.stopTime = start + duration
        self.phrases = phrases
        self.phrase = phrases[languages.ENGLISH]

    def draw(self, frame, image):
        if (frame < self.startTime or frame >= self.stopTime):
            return
        idx = frame - self.startTime
        factor = self.phrase[1]
        textMask = self.phrase[0](int(idx * factor))
        image.paste("black", (810, 115), textMask)

    def set_language(self, language):
        ':type language: languages'
        if language == languages.ENGLISH:
            self.phrase = self.phrases[languages.ENGLISH]
        elif language == languages.SPANISH:
            self.phrase = self.phrases[languages.SPANISH]


class apple:
    def __init__(self, start, stop, position):
        self.startTime = start
        self.stopTime = stop
        self.position = position
        self.image = Image.open("./images/apple.png")

    def draw(self, frame, image):
        if (frame < self.startTime or frame >= self.stopTime):
            return
        idx = frame - self.startTime
        sz = min(idx, 35)
        apple = self.image.resize((sz, sz), Image.ANTIALIAS)
        image.paste(apple, (self.position[0] - sz / 2, self.position[1]), apple)


class lupa:
    def __init__(self, start, stop, positionsAndPhrases):
        self.startTime = start
        self.stopTime = stop
        self.language = languages.ENGLISH
        self.positionsAndPhrases = positionsAndPhrases
        self.lupa = Image.open("./images/lupa.png")
        self.mask = Image.open("./images/mask.png").convert("L")
        self.base = Image.open("./images/base10.png")
        self.apple = Image.open("./images/apple.png").resize((350, 350), Image.ANTIALIAS)

    def draw(self, frame, image):
        if (frame < self.startTime or frame >= self.stopTime):
            return
        idx = frame - self.startTime
        [idx1, idx2] = divmod(idx, 40)
        k = math.pow(math.sin(math.pi / 2. * idx2 / 39.), 12 if idx1 != 0 else 1)
        if idx1 + 2 > len(self.positionsAndPhrases):
            x = self.positionsAndPhrases[int(idx1)][0][0]
            y = self.positionsAndPhrases[int(idx1)][0][1]
        else:
            x = int((1 - k) * self.positionsAndPhrases[int(idx1)][0][0] + k * (
            self.positionsAndPhrases[int(idx1 + 1)][0][0]))
            y = int((1 - k) * self.positionsAndPhrases[int(idx1)][0][1] + k * (
            self.positionsAndPhrases[int(idx1 + 1)][0][1]))
        area = self.base.crop((x - 218 / 5, y - 218 / 5, x + 218 / 5, y + 218 / 5))
        area = area.resize((218 * 2, 2 * 218), Image.ANTIALIAS)
        for positionAndPhrase in self.positionsAndPhrases:
            ax = positionAndPhrase[0][0]
            ay = positionAndPhrase[0][1]
            textMasks = positionAndPhrase[1]
            if textMasks != None:
                textMask = textMasks[self.language]
                pos = (43 - 5 * (x - ax) - 10, 43 - 5 * (y - ay))
                awt = self.apple.copy()
                awt.paste("white", (165 - textMask.size[0] / 2, 150), textMask)
                area.paste(awt, pos, awt)
        image.paste(area, (x - 218, y - 218), self.mask)
        image.paste(self.lupa, (x - 254, y - 244), self.lupa)

    def set_language(self, language):
        ':type language: languages'
        self.language = language


class evolve(evolve_base):
    font = aggdraw.Font("white", "./fonts/calibri.ttf", 46)
    text_english = [u"In just 1.5 years, ", u"the Region's", u"indigenous women", u"and PSYDEH have",
                    u"dismantled walls,", u"planted seeds and", u"dream of fruits", u"to come."]
    text_spanish = [u"En solo un a\u00f1o y medio,", u"las mujeres ind\u00edgenas", u"de la Regi\u00f3n y PSYDEH",
                    u"han desmantelado las", u"paredes, plantado", u"semillas y sue\u00f1an con",
                    u"los frutos que brotar\u00e1n."]

    phrase1 = {languages.ENGLISH: [Phrases().makeImage_runnable(text_english, font, 46), 1.0],
               languages.SPANISH: [Phrases().makeImage_runnable(text_spanish, font, 46),
                                   Helpers.getLetterRatio(text_english, text_spanish)]}

    def __init__(self, start):
        self.startTime = start
        self.stopTime = start + 430
        self.list = []
        positions = [(600, 950), (400, 237), (600, 333), (396, 380), (568, 193), (529, 352), (663, 238),
                     (409, 304)]  # ,(723,372)]
        phrases = [None]

        phrases.append({languages.ENGLISH: [u"sustainable", u"economic", u"development"],
                        languages.SPANISH: [u"Desarrollo", u"econ\u00f3mico", u"sustentable."]})
        phrases.append({languages.ENGLISH: [u"education", u"that", u"empowers"],
                        languages.SPANISH: [u"Educaci\u00f3n", u"que", u"fortalece."]})
        phrases.append({languages.ENGLISH: [u"protected rights", u"and", u"justice"],
                        languages.SPANISH: [u"Protecci\u00f3n de", u"derechos y justicia."]})
        phrases.append({languages.ENGLISH: [u"healthy relations", u"between", u"women and men"],
                        languages.SPANISH: [u"Relaciones saludables", u"entre mujeres", u"y hombres."]})
        phrases.append(
            {languages.ENGLISH: [u"responsible", u"government"], languages.SPANISH: [u"Gobierno", u"responsable."]})
        phrases.append(
            {languages.ENGLISH: [u"protected", u"environment"], languages.SPANISH: [u"Medio ambiente", u"protegido."]})
        phrases.append({languages.ENGLISH: [u"quality", u"health", u"care"],
                        languages.SPANISH: [u"Sistema", u"de salud", u"de calidad."]})
        # phrases.append(["umbrella network","of","local NGOs"])
        self.list.append(still(start))
        self.list.append(text(start, 430, self.phrase1))
        self.list.append(apple(start + 70, start + 410, positions[1]))  # could put the commands into a loop
        self.list.append(apple(start + 75, start + 410, positions[2]))
        self.list.append(apple(start + 80, start + 410, positions[3]))
        self.list.append(apple(start + 85, start + 410, positions[4]))
        self.list.append(apple(start + 90, start + 410, positions[5]))
        self.list.append(apple(start + 95, start + 410, positions[6]))
        # self.list.append(apple(start + 100, start + 450, positions[7] ))
        self.list.append(lupa(start + 110, start + 430, self.zipper(positions, phrases)))
        self.list.append(
            Transitions.pageFlip(Image.open("./images/base12.png").convert("RGBA"), None, start + 410, 20, True))

    def zipper(self, a, b):
        font = aggdraw.Font("white", "./fonts/sans.ttf", 28)
        phrases = Phrases()
        retArray = []
        for pos, texts in zip(a, b):
            l_dict = {}
            if texts == None:
                retArray.append([pos, None])
            else:
                for language in languages.list_of_languages:
                    l_dict[language] = phrases.makeImage_centered(texts[language], font)
                retArray.append([pos, l_dict])
        return retArray
