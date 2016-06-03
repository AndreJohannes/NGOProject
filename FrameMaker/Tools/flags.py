from PIL import Image


class Flags:
    AMERICA = 1
    ARGENTINA = 2
    AUSTRALIA = 3
    BRAZIL = 4
    GERMANY = 5
    GUATEMALA = 6
    HONDURAS = 7
    NIGERIA = 8
    RUSSIA = 9
    SCOTTLAND = 10
    SPAIN = 11
    MEXICO = 12
    BRITAIN = 13
    JAPAN = 14
    KIWI = 15

    def __init__(self):
        pass

    def getFlag(self, code):
        if code == self.AMERICA:
            return self.getAmericanFlag()
        elif code == self.ARGENTINA:
            return self.getArgentinanFlag()
        elif code == self.AUSTRALIA:
            return self.getAustralianFlag()
        elif code == self.BRAZIL:
            return self.getBrazilianFlag()
        elif code == self.SPAIN:
            return self.getSpanishFlag()
        elif code == self.BRITAIN:
            return self.getBritishFlag()
        elif code == self.JAPAN:
            return self.getJapaneseFlag()
        elif code == self.RUSSIA:
            return self.getRussianFlag()
        elif code == self.HONDURAS:
            return self.getHonduranFlag()
        elif code == self.MEXICO:
            return self.getMexicanFlag()

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

    @staticmethod
    def getUNFlag():
        image = Image.open("./Flags/unitedNations.png")
        return image.resize((91, 58)).convert("RGBA")

    @staticmethod
    def getDoveFlag():
        image = Image.open("./Flags/dove.png")
        return image.resize((91, 58), Image.ANTIALIAS).convert("RGBA")

    @staticmethod
    def getiDoveFlag():
        image = Image.open("./Flags/dove_inverse.png")
        return image.resize((91, 58), Image.ANTIALIAS).convert("RGBA")
