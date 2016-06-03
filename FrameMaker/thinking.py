from PIL import Image
import aggdraw
from Tools.phrases import Phrases
import Tools.tools as Tools
from Tools.frontender import languages, evolve_base
from Tools.flags import Flags
from pango import Language


class evolve(evolve_base):
    font = aggdraw.Font("white", "./fonts/font1.ttf", 46)
    phrase1 = {languages.ENGLISH: Phrases().makeImage([u"We build a wall?", u"     Really?"], font),
               languages.SPANISH: Phrases().makeImage([u"\u00bfConstruimos una pared?", u"     \u00bfEn serio?"], font),
               languages.GERMAN: Phrases().makeImage([u"Wir errichten eine Mauer?", u"  Wirklich?"], font)}
    phrase2 = {languages.ENGLISH: Phrases().makeImage([u"What are people like", u"on the other side?"], font),
               languages.SPANISH: Phrases().makeImage([u"\u00bfComo es la gente del otro lado?"], font),
               languages.GERMAN: Phrases().makeImage([u"Wie sind die Leute", u"auf der anderen Seite?"], font)}
    phrase3 = {languages.ENGLISH: Phrases().makeImage([u"American"], font),
               languages.SPANISH: Phrases().makeImage([u"Americano"], font),
               languages.GERMAN: Phrases().makeImage([u"Amerikaner"], font)}
    phrase4 = {languages.ENGLISH: Phrases().makeImage([u"Mexican"], font),
               languages.SPANISH: Phrases().makeImage([u"Mexicano"], font),
               languages.GERMAN: Phrases().makeImage([u"Mexikaner"], font)}
    phrase5 = {languages.ENGLISH: Phrases().makeImage([u"Latinos, Europeans", u"  or Asians"], font),
               languages.SPANISH: Phrases().makeImage([u"Latinos, Europeos", u"  o Asi\u00e1ticos"], font),
               languages.GERMAN: Phrases().makeImage([u"Latinos, Europ\u00e4er", u"oder Asiaten"], font)}
    phrase6 = {languages.ENGLISH: Phrases().makeImage([u"We are so", u"different."], font),
               languages.SPANISH: Phrases().makeImage([u"Somos tan", u"diferentes"], font),
               languages.GERMAN: Phrases().makeImage([u"Wir sind so", u"verschieden"], font)}

    def __init__(self, start):
        self.startTime = start
        self.stopTime = start + 270
        self.image = Image.open("./images/base1.png")
        d = aggdraw.Draw(self.image)
        p = aggdraw.Pen("black", 8.46666)
        d.ellipse((640 - 315, 596, 640 + 315, 596), p)
        d.flush()
        self.thoughts = [Tools.OneThought(start + 0, self.phrase1, 380)]
        self.thoughts.append(Tools.OneThought(start + 30, self.phrase2, 945))
        self.thoughts.append(Tools.OneThought(start + 60, self.phrase3, 380))
        self.thoughts.append(Tools.OneThought(start + 90, self.phrase4, 945))
        self.thoughts.append(Tools.OneThought(start + 120, self.phrase5, 380))
        self.thoughts.append(Tools.OneThought(start + 150, self.phrase6, 945))

        self.thoughts.append(Tools.OneFlag(start + 100, start + 170, Flags.AMERICA, 462, 349))
        self.thoughts.append(Tools.OneFlag(start + 130, start + 200, Flags.MEXICO, 826, 349))

        self.thoughts.append(Tools.OneFlag(start + 150, start + 200, Flags.MEXICO, 462, 349))
        self.thoughts.append(Tools.OneFlag(start + 170, start + 230, Flags.AUSTRALIA, 462, 349))
        self.thoughts.append(Tools.OneFlag(start + 190, start + 260, Flags.SPAIN, 462, 349))
        self.thoughts.append(Tools.OneFlag(start + 210, start + 300, Flags.JAPAN, 462, 349))
        # self.thoughts.append(Tools.OneFlag(start + 230, start + 380, "dove", 462, 349))

        self.thoughts.append(Tools.OneFlag(start + 175, start + 245, Flags.BRITAIN, 826, 349))
        self.thoughts.append(Tools.OneFlag(start + 195, start + 275, Flags.HONDURAS, 826, 349))
        self.thoughts.append(Tools.OneFlag(start + 215, start + 315, Flags.RUSSIA, 826, 349))
        # self.thoughts.append(Tools.OneFlag(start + 205, start + 380, "idove", 826, 349))

        self.thoughts.append(Tools.ThoughtfulTransition(start + 180, Image.open("./images/base2.png"), 380))
        self.list = self.thoughts

    def draw(self, frame, image):
        if (frame < self.startTime or frame >= self.stopTime):
            return
        image.paste(self.image, (0, 0))
        for though in self.thoughts:
            though.draw(frame, image)
