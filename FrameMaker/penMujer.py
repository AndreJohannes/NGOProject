import aggdraw
from PIL import Image

import Tools.tools as Tools
from Tools.frontender import evolve_base, languages
from Tools.phrases import Phrases


class OneThought:
    def __init__(self, startTime, images, pos_x, left, down=False):
        self.images = images
        self.bubble = Tools.MovingBubble(pos_x, 163, 10, startTime, 20, left, down)
        pos_x += -100 if left else 100
        self.rectangualar = Tools.MorphingTextBox(images[languages.ENGLISH], pos_x, 139 if down is False else 243, 20, startTime + 20, True)

    def draw(self, frame, image):
        self.bubble.draw(frame, image)
        self.rectangualar.draw(frame, image)

    def set_language(self, language):
        ':type language: languages'
        self.rectangualar.image = self.images[language]


class pensativo:
    def __init__(self, start):
        self.startTime = start
        self.stopTime = start + 130

    def draw(self, frame, image):
        if (frame < self.startTime or frame >= self.stopTime):
            return
        idx = frame - self.startTime
        im = Image.open("../Pensombre/images/pensativo/image{}.png".format(min(idx, 69)))
        image.paste(im, (0, 0))


class rolling_tl:
    def __init__(self, start):
        self.startTime = start
        self.stopTime = start + 65

    def draw(self, frame, image):
        if (frame < self.startTime or frame >= self.stopTime):
            return
        idx = frame - self.startTime
        im = Image.open("../Pensombre/images/rollingeyes/topleft/image{}.png".format(min(idx, 5))).crop(
            (0, 0, 800, 360))
        image.paste(im, (0, 0))


class rolling_tlb:
    def __init__(self, start):
        self.startTime = start
        self.stopTime = start + 20

    def draw(self, frame, image):
        if (frame < self.startTime or frame >= self.stopTime):
            return
        idx = frame - self.startTime
        im = Image.open("../Pensombre/images/rollingeyes/topleft/image{}.png".format(max(5 - idx, 0))).crop(
            (0, 0, 800, 360))
        image.paste(im, (0, 0))


class slider:
    def __init__(self, start):
        self.startTime = start
        self.stopTime = start + 26

    def draw(self, frame, image):
        if (frame < self.startTime or frame >= self.stopTime):
            return

        idx = frame - self.startTime
        base = Image.open("./images/slider/image" + "{:02d}".format(max(min(idx, 26), 0)) + ".png")
        image.paste(base, (0, 0))
        dic = {10: 1221, 11: 1196, 12: 1153, 13: 1096, 14: 1022, 15: 952, 16: 874, 17: 797, 18: 724, 19: 646, 20: 562,
               21: 476, 22: 391, 23: 297, 24: 208, 25: 80}
        if (dic.has_key(idx)):
            base2 = Image.open("./images/base3.png")
            mask = Image.new("L", (1280, 720), "white")
            mask.paste("black", (0, 0, dic[idx], 720))
            image.paste(base2, (0, 0), mask)


class evolve(evolve_base):
    font = aggdraw.Font("white", "./fonts/font1.ttf", 46)
    phrase1 = {languages.ENGLISH: Phrases().makeImage([u"If I could remove", u"blocks from the wall...?"], font),
               languages.SPANISH: Phrases().makeImage([u"\u00bfSi pudiera quitar los", u"ladrillos de la pared...?"],
                                                      font),
               languages.GERMAN: Phrases().makeImage(
                   [u"Wenn ich nur die Ziegel von", u"der Wand nehmen k\u00f6nnte...?"],
                   font)}
    phrase2 = {
        languages.ENGLISH: Phrases().makeImage([u"AND if the person on the", u"other side does the same..."], font),
        languages.SPANISH: Phrases().makeImage([u"Y si la persona del", u"otro lado hiciera lo mismo..."], font),
        languages.GERMAN: Phrases().makeImage([u"UND wenn die Person auf der", u"anderen Seite das gleiche tut...."],
                                              font)}
    phrase3 = {languages.ENGLISH: Phrases().makeImage([u"We can actually grow", u"the sustainable!"], font),
               languages.SPANISH: Phrases().makeImage([u"\u00a1De hecho podemos", u"crecer sustentablemente!"], font),
               languages.GERMAN: Phrases().makeImage(
                   [u"Koennen wir tats\u00e4chlich", u"etwas nachhaltiges erschaffen!"],
                   font)}

    def __init__(self, start):
        self.startTime = start
        self.stopTime = start + 156
        self.list = []
        self.list.append(pensativo(start))
        self.list.append(rolling_tl(start + 10))
        self.list.append(rolling_tlb(start + 75))
        self.list.append(slider(start + 130))
        self.list.append(OneThought(start + 0, self.phrase1, 500, True))
        self.list.append(OneThought(start + 30, self.phrase2, 877, False))
        self.list.append(OneThought(start + 60, self.phrase3, 500, True, True))
