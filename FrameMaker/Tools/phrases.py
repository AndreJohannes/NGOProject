from PIL import Image
import aggdraw


class Phrases:
    def __init__(self):
        self.image = Image.new("L", (1280, 720), "black")

    def getPhrase(self, name):
        return self.dict[name]

    @staticmethod
    def getPhrase32(i):
        image = Image.new("L", (1150, 205), "black")
        d = aggdraw.Draw(image)
        font = aggdraw.Font("white", "./fonts/sans.ttf", 26)
        text = ["         Umbrella"]
        text.append("  Network of")
        text.append("  five Indigenous")
        text.append("  Women-led")
        text.append("Organizations")
        offset = 0
        offsetY = 0
        for frag in text:
            d.text((10, offsetY), frag[0:max(i - offset, 0)], font)
            offsetY += 30
            offset += len(frag)
        d.flush()
        return image

    @staticmethod
    def getPhrase33(i):
        image = Image.new("L", (1150, 205), "black")
        d = aggdraw.Draw(image)
        font = aggdraw.Font("white", "./fonts/sans.ttf", 26)
        text = ["  Regional"]
        text.append("Development")
        text.append("  Agenda")
        offset = 0
        offsetY = 0
        for frag in text:
            d.text((10, offsetY), frag[0:max(i - offset, 0)], font)
            offsetY += 30
            offset += len(frag)
        d.flush()
        return image

    @staticmethod
    def getPhrase34(i):
        image = Image.new("L", (1150, 205), "black")
        d = aggdraw.Draw(image)
        font = aggdraw.Font("white", "./fonts/sans.ttf", 26)
        text = ["Regional "]
        text.append(" Cooperative")
        text.append("   of Artisans")
        offset = 0
        offsetY = 0
        for frag in text:
            d.text((10, offsetY), frag[0:max(i - offset, 0)], font)
            offsetY += 30
            offset += len(frag)
        d.flush()
        return image

    @staticmethod
    def getPhrase35(i):
        image = Image.new("L", (1150, 205), "black")
        d = aggdraw.Draw(image)
        font = aggdraw.Font("white", "./fonts/sans.ttf", 26)
        text = ["Annual"]
        text.append("  Indigenous")
        text.append("      Women")
        text.append("	       Forums")
        offset = 0
        offsetY = 0
        for frag in text:
            d.text((10, offsetY), frag[0:max(i - offset, 0)], font)
            offsetY += 30
            offset += len(frag)
        d.flush()
        return image

    @staticmethod
    def getPhrase50(i):
        image = Image.new("L", (1150, 605), "black")
        d = aggdraw.Draw(image)
        font = aggdraw.Font("white", "./fonts/calibri.ttf", 46)
        text = ["Five new local projects by the Umbrella"]
        text.append("Network's women-led organizations.")
        offset = 0
        offsetY = 0
        for frag in text:
            d.text((10, offsetY), frag[0:max(i - offset, 0)], font)
            offsetY += 50
            offset += len(frag)
        d.flush()
        return image

    @staticmethod
    def getPhrase51(i):
        image = Image.new("L", (1150, 605), "black")
        d = aggdraw.Draw(image)
        font = aggdraw.Font("white", "./fonts/calibri.ttf", 46)
        text = ["Training program for the Regional"]
        text.append("Cooperative of Indigenous Artisans.")
        offset = 0
        offsetY = 0
        for frag in text:
            d.text((10, offsetY), frag[0:max(i - offset, 0)], font)
            offsetY += 50
            offset += len(frag)
        d.flush()
        return image

    @staticmethod
    def getPhrase52(i):
        image = Image.new("L", (1150, 605), "black")
        d = aggdraw.Draw(image)
        font = aggdraw.Font("white", "./fonts/calibri.ttf", 46)
        text = ["Narrative development program"]
        text.append("for the Network's women leaders.")
        offset = 0
        offsetY = 0
        for frag in text:
            d.text((10, offsetY), frag[0:max(i - offset, 0)], font)
            offsetY += 50
            offset += len(frag)
        d.flush()
        return image

    @staticmethod
    def getPhrase55(i):
        image = Image.new("L", (790, 160), "black")
        d = aggdraw.Draw(image)
        font = aggdraw.Font("white", "./fonts/calibrib.ttf", 46)
        text = []
        text.append("www.psydeh.com")
        offset = 0
        offsetY = 0
        for frag in text:
            d.text((10, offsetY), frag[0:max(i - offset, 0)], font)
            offsetY += 50
            offset += len(frag)
        d.flush()
        return image

    def makeImage(self, listOfText, font, space_h=None):
        testCanvas = aggdraw.Draw(self.image)
        size_x = 0
        size_y = 0
        for text in listOfText:
            size = testCanvas.textsize(text, font)
            size_x = max(size_x, size[0])
            dy = size[1]
            size_y += size[1]
        image = Image.new("L", (int(size_x + 20), int(size_y)), "black")
        d = aggdraw.Draw(image)
        yoffset = 0
        if space_h != None:
            dy = space_h
        for text in listOfText:
            d.text((10, yoffset), text, font)
            yoffset += dy
        d.flush()
        return image

    def makeImage_centered(self, listOfText, font):
        testCanvas = aggdraw.Draw(self.image)
        size_x = 0
        size_y = 0
        for text in listOfText:
            size = testCanvas.textsize(text, font)
            size_x = max(size_x, size[0])
            dy = size[1]
            size_y += size[1]
        image = Image.new("L", (int(size_x + 20), int(size_y)), "black")
        d = aggdraw.Draw(image)
        yoffset = 0
        for text in listOfText:
            size = testCanvas.textsize(text, font)
            d.text(((20 + size_x - size[0]) / 2, yoffset), text, font)
            yoffset += dy
        d.flush()
        return image

    def makeImage_centered_runnable(self, listOfText, font):
        ':type font: aggdraw.Font'
        testCanvas = aggdraw.Draw(self.image)
        size_x = 0
        size_y = 0
        for text in listOfText:
            size = testCanvas.textsize(text, font)
            size_x = max(size_x, size[0])
            dy = size[1]
            size_y += size[1]
        size_t = (int(size_x + 20), int(size_y))

        def getImage(idx):
            image = Image.new("L", size_t, "black")
            d = aggdraw.Draw(image)
            yoffset = 0
            offset = 0
            for text in listOfText:
                size = testCanvas.textsize(text, font)
                d.text(((size_t[0] - size[0]) / 2, yoffset), text[0:max(idx - offset, 0)], font)
                yoffset += dy
                offset += len(text)
            d.flush()
            return image

        return getImage

    def makeImage_runnable(self, listOfText, font, space_h=None):
        ':type font: aggdraw.Font'
        testCanvas = aggdraw.Draw(self.image)
        size_x = 0
        size_y = 0
        for text in listOfText:
            size = testCanvas.textsize(text, font)
            size_x = max(size_x, size[0])
            dy = size[1]
            size_y += size[1]
        size_t = (int(size_x + 20), int(size_y))
        if space_h != None:
            dy = space_h

        def getImage(idx):
            image = Image.new("L", size_t, "black")
            d = aggdraw.Draw(image)
            yoffset = 0
            offset = 0
            for text in listOfText:
                size = testCanvas.textsize(text, font)
                d.text((0, yoffset), text[0: max(idx - offset, 0)], font)
                yoffset += dy
                offset += len(text)
            d.flush()
            return image

        return getImage

# Phrases.getPhrase26(50).show()
