from PIL import Image
from PIL import ImageDraw
import aggdraw
import math
import random


class Flags:
    def __init__(self):
        self.dict = {}
        self.dict["america"] = Flags.getAmericanFlag()
        self.dict["argentina"] = Flags.getArgentinanFlag()
        self.dict["australia"] = Flags.getAustralianFlag()
        self.dict["brazil"] = Flags.getBrazilianFlag()
        self.dict["germany"] = Flags.getGermanFlag()
        self.dict["guatemala"] = Flags.getGuatelmalanFlag()
        self.dict["honduras"] = Flags.getHonduranFlag()
        self.dict["namerica"] = Flags.getNamericanFlag()
        self.dict["nigeria"] = Flags.getNigerianFlag()
        self.dict["russia"] = Flags.getRussianFlag()
        self.dict["scottland"] = Flags.getScottishFlag()
        self.dict["spain"] = Flags.getSpanishFlag()
        self.dict["mexican"] = Flags.getMexicanFlag()
        self.dict["british"] = Flags.getBritishFlag()
        self.dict["japanese"] = Flags.getJapaneseFlag()
        self.dict["kiwi"] = Flags.getKiwiFlag()

    def getFlag(self, name):
        return self.dict[name]

    @staticmethod
    def getAmericanFlag():
        image = Image.open("./Flags/america.png")
        return image.resize((91, 58)).convert("RGBA")

    @staticmethod
    def getArgentinanFlag():
        image = Image.open("./Flags/argentina.png")
        return image.resize((91, 58)).convert("RGBA")

    @staticmethod
    def getAustralianFlag():
        image = Image.open("./Flags/australia.png")
        return image.resize((91, 58)).convert("RGBA")

    @staticmethod
    def getBrazilianFlag():
        image = Image.open("./Flags/brazil.png")
        return image.resize((91, 58)).convert("RGBA")

    @staticmethod
    def getGermanFlag():
        image = Image.open("./Flags/german.png")
        return image.resize((91, 58)).convert("RGBA")

    @staticmethod
    def getGuatelmalanFlag():
        image = Image.open("./Flags/guatemala.png")
        return image.resize((91, 58)).convert("RGBA")

    @staticmethod
    def getHonduranFlag():
        image = Image.open("./Flags/honduras.png")
        return image.resize((91, 58)).convert("RGBA")

    @staticmethod
    def getNamericanFlag():
        image = Image.open("./Flags/namerican.png")
        return image.resize((91, 58)).convert("RGBA")

    @staticmethod
    def getNigerianFlag():
        image = Image.open("./Flags/nigeria.png")
        return image.resize((91, 58)).convert("RGBA")

    @staticmethod
    def getRussianFlag():
        image = Image.open("./Flags/russian.png")
        return image.resize((91, 58)).convert("RGBA")

    @staticmethod
    def getScottishFlag():
        image = Image.open("./Flags/scottish.png")
        return image.resize((91, 58)).convert("RGBA")

    @staticmethod
    def getSpanishFlag():
        image = Image.open("./Flags/spanish.png")
        return image.resize((91, 58)).convert("RGBA")

    @staticmethod
    def getMexicanFlag():
        image = Image.open("./Flags/mexican.png")
        return image.resize((91, 58)).convert("RGBA")

    @staticmethod
    def getJapaneseFlag():
        image = Image.open("./Flags/japan.png")
        return image.resize((91, 58)).convert("RGBA")

    @staticmethod
    def getKiwiFlag():
        image = Image.open("./Flags/kiwi.png")
        return image.resize((91, 58)).convert("RGBA")

    @staticmethod
    def getBritishFlag():
        image = Image.open("./Flags/british.png")
        return image.resize((91, 58)).convert("RGBA")
