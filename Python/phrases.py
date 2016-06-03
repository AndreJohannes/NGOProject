from PIL import Image
from PIL import ImageDraw
import aggdraw
import math


class Phrases:
    def __init__(self):
        self.image = Image.new("L", (1280, 720), "black")

    def getPhrase(self, name):
        return self.dict[name]

    @staticmethod
    def getPhrase2():
        font = aggdraw.Font("white", "font1.ttf", 46)
        texts = ["We build a wall?", "     Really?"]
        return Phrases().makeImage(texts, font)

    @staticmethod
    def getPhrase3():
        font = aggdraw.Font("white", "font1.ttf", 46)
        texts = ["What are people like", "on the other side?"]
        return Phrases().makeImage(texts, font)

    @staticmethod
    def getPhrase4():
        font = aggdraw.Font("white", "font1.ttf", 46)
        texts = ["How can we", "engage?"]
        return Phrases().makeImage(texts, font)

    @staticmethod
    def getPhrase5():
        font = aggdraw.Font("white", "font1.ttf", 46)
        texts = ["I am only one", "person."]
        return Phrases().makeImage(texts, font)

    @staticmethod
    def getPhrase6():
        font = aggdraw.Font("white", "font1.ttf", 46)
        texts = ["American"]
        return Phrases().makeImage(texts, font)

    @staticmethod
    def getPhrase7():
        font = aggdraw.Font("white", "font1.ttf", 46)
        texts = ["Mexican"]
        return Phrases().makeImage(texts, font)

    @staticmethod
    def getPhrase8():
        font = aggdraw.Font("white", "font1.ttf", 46)
        texts = ["Argentinian"]
        return Phrases().makeImage(texts, font)

    @staticmethod
    def getPhrase9():
        font = aggdraw.Font("white", "font1.ttf", 46)
        texts = ["Briton"]
        return Phrases().makeImage(texts, font)

    @staticmethod
    def getPhrase10():
        font = aggdraw.Font("white", "font1.ttf", 46)
        texts = ["German"]
        return Phrases().makeImage(texts, font)

    @staticmethod
    def getPhrase11():
        font = aggdraw.Font("white", "font1.ttf", 46)
        texts = ["Spaniard"]
        return Phrases().makeImage(texts, font)

    @staticmethod
    def getPhrase12():
        font = aggdraw.Font("white", "font1.ttf", 46)
        texts = ["Japanese"]
        return Phrases().makeImage(texts, font)

    @staticmethod
    def getPhrase13():
        font = aggdraw.Font("white", "font1.ttf", 46)
        texts = ["Kiwi"]
        return Phrases().makeImage(texts, font)

    @staticmethod
    def getPhrase14():
        font = aggdraw.Font("white", "font1.ttf", 46)
        texts = ["We are so", "different."]
        return Phrases().makeImage(texts, font)

    @staticmethod
    def getPhrase15():
        font = aggdraw.Font("white", "font1.ttf", 46)
        texts = ["The world", "changes."]
        return Phrases().makeImage(texts, font)

    @staticmethod
    def getPhrase16():
        image = Image.new("L", (180, 60), "black")
        d = aggdraw.Draw(image)
        font = aggdraw.Font("white", "font1.ttf", 36)
        d.text((10, 0), "Differences and", font)
        d.text((30, 25), "change are scary.", font)
        d.flush()
        return image

    @staticmethod
    def getPhrase17():
        font = aggdraw.Font("white", "font1.ttf", 46)
        texts = ["But what are people like", "on the other side?"]
        return Phrases().makeImage(texts, font)

    @staticmethod
    def getPhrase18():
        font = aggdraw.Font("white", "font1.ttf", 46)
        texts = ["All walls are made", "of blocks."]
        return Phrases().makeImage(texts, font)
        image = Image.new("L", (170, 60), "black")

    @staticmethod
    def getPhrase19():
        font = aggdraw.Font("white", "font1.ttf", 46)
        texts = ["Violence, fear, poverty, ignorance", "and technology isolation,"]
        return Phrases().makeImage(texts, font)

    @staticmethod
    def getPhrase20():
        font = aggdraw.Font("white", "font1.ttf", 46)
        texts = ["These blocks divide."]
        return Phrases().makeImage(texts, font)

    @staticmethod
    def getPhrase21():
        font = aggdraw.Font("white", "font1.ttf", 46)
        texts = ["If I could remove the", "blocks from the wall...?"]
        return Phrases().makeImage(texts, font)

    @staticmethod
    def getPhrase22a():
        font = aggdraw.Font("white", "font1.ttf", 46)
        texts = ["AND if the person on the", "other side does the same..."]
        return Phrases().makeImage(texts, font)

    @staticmethod
    def getPhrase22b():
        font = aggdraw.Font("white", "font1.ttf", 46)
        texts = ["We build the sustainable..."]
        return Phrases().makeImage(texts, font)

    @staticmethod
    def getPhrase23():
        font = aggdraw.Font("white", "font1.ttf", 46)
        texts = ["We ARE better in collaboration.", "It is science!"]
        return Phrases().makeImage(texts, font)

    @staticmethod
    def getPhrase24(i):
        image = Image.new("L", (1150, 205), "black")
        d = aggdraw.Draw(image)
        font = aggdraw.Font("white", "adler.ttf", 36)
        text = ["Hidalgo is a small, ruggedly beautiful state in"]
        text.append("central Mexico. There, indigenous citizens are")
        text.append("spread among three regions in which human")
        text.append("development levels are near the lowest in the")
        text.append("world:")
        offset = 0
        offsetY = 0
        for frag in text:
            d.text((10, offsetY), frag[0:max(i - offset, 0)], font)
            offsetY += 40
            offset += len(frag)
        d.flush()
        return image

    @staticmethod
    def getPhrase25(i):
        image = Image.new("L", (850, 95), "black")
        d = aggdraw.Draw(image)
        font = aggdraw.Font("white", "adler.ttf", 36)
        text = [u"In the Otomi-Tepehua region"]
        text.append("sit four majority indigenous areas.")
        offset = 0
        offsetY = 0
        for frag in text:
            d.text((10, offsetY), frag[0:max(i - offset, 0)], font)
            offsetY += 40
            offset += len(frag)
        d.flush()
        return image

    @staticmethod
    def getPhrase26(i):
        image = Image.new("L", (1150, 905), "black")
        d = aggdraw.Draw(image)
        font = aggdraw.Font("white", "adler.ttf", 36)
        text = ["-For centuries the Region's indigenous citizens"]
        text.append(" have been seperated by walls, dividing community")
        text.append(" from community and the Region from the world.")
        text.append("             ")
        text.append("-As many as 86% of the Region's people earn less")
        text.append("  than $96usd per month.")
        text.append("             ")
        text.append("-Less than 1% of homes possess a computer.")
        text.append("             ")
        text.append("-Communities rarely collaborate, municipalities")
        text.append(" even less. Women average four grades of schooling")
        text.append(" and are not supported as leaders.")
        offset = 0
        offsetY = 0
        for frag in text:
            d.text((10, offsetY), frag[0:max(i - offset, 0)], font)
            offsetY += 40
            offset += len(frag)
        d.flush()
        return image

    @staticmethod
    def getPhrase27(i):
        image = Image.new("L", (1150, 770), "black")
        d = aggdraw.Draw(image)
        font = aggdraw.Font("white", "adler.ttf", 36)
        text = ["-Since 2013, Nahua, Otomi and Tepehua citizens"]
        text.append(" have defied the walls and build their own bottom-")
        text.append(" up rights-based movement.")
        text.append("             ")
        text.append("-In partnership with the Mexican NGO PSYDEH, in")
        text.append(" 2014 and 2015, a network of 500+ indigenous woman")
        text.append(" from 35+ communities planted innovative seeds for")
        text.append(" their sustainable future.")
        offset = 0
        offsetY = 0
        for frag in text:
            d.text((10, offsetY), frag[0:max(i - offset, 0)], font)
            offsetY += 40
            offset += len(frag)
        d.flush()
        return image

    @staticmethod
    def getPhrase28(i):
        image = Image.new("L", (1150, 605), "black")
        d = aggdraw.Draw(image)
        font = aggdraw.Font("white", "adler.ttf", 36)
        text = ["These seeds = learning about: "]
        text.append("             ")
        text.append("   - shared realities")
        text.append("             ")
        text.append("   - clarity on solutions to problems")
        text.append("             ")
        text.append("   - leader disciplines needed to implement")
        text.append("     solutions")
        text.append("             ")
        text.append("   - rights & laws on which solutions are based")
        text.append("             ")
        text.append("   - personal & communal autonomy, including ")
        text.append("     how to negociate with government")

        offset = 0
        offsetY = 0
        for frag in text:
            d.text((10, offsetY), frag[0:max(i - offset, 0)], font)
            offsetY += 40
            offset += len(frag)
        d.flush()
        return image

    @staticmethod
    def getPhrase29(i):
        image = Image.new("L", (1150, 205), "black")
        d = aggdraw.Draw(image)
        font = aggdraw.Font("white", "adler.ttf", 36)
        text = ["Where walls once existed, seeds have been planted"]
        text.append("and a tree grows.")
        offset = 0
        offsetY = 0
        for frag in text:
            d.text((10, offsetY), frag[0:max(i - offset, 0)], font)
            offsetY += 40
            offset += len(frag)
        d.flush()
        return image

    @staticmethod
    def getPhrase30(i):
        image = Image.new("L", (1150, 205), "black")
        d = aggdraw.Draw(image)
        font = aggdraw.Font("white", "adler.ttf", 36)
        text = ["This tree, a metaphor for sustainable life,"]
        text.append("symbolizes our movement's work.")
        offset = 0
        offsetY = 0
        for frag in text:
            d.text((10, offsetY), frag[0:max(i - offset, 0)], font)
            offsetY += 40
            offset += len(frag)
        d.flush()
        return image

    @staticmethod
    def getPhrase31(i):
        image = Image.new("L", (1150, 205), "black")
        d = aggdraw.Draw(image)
        font = aggdraw.Font("white", "adler.ttf", 36)
        text = ["As the tree grows, it buds splendid new leaves:"]
        offset = 0
        offsetY = 0
        for frag in text:
            d.text((10, offsetY), frag[0:max(i - offset, 0)], font)
            offsetY += 40
            offset += len(frag)
        d.flush()
        return image

    @staticmethod
    def getPhrase32(i):
        image = Image.new("L", (1150, 205), "black")
        d = aggdraw.Draw(image)
        font = aggdraw.Font("white", "sans.ttf", 26)
        text = ["         Five"]
        text.append("new indigenous")
        text.append("   women-led")
        text.append("organizations")
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
        font = aggdraw.Font("white", "sans.ttf", 26)
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
        font = aggdraw.Font("white", "sans.ttf", 26)
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
        font = aggdraw.Font("white", "sans.ttf", 26)
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
    def getPhrase36(i):
        image = Image.new("L", (570, 405), "black")
        d = aggdraw.Draw(image)
        font = aggdraw.Font("white", "adler.ttf", 36)
        text = ["In just 1.5 years, "]
        text.append("the Region's")
        text.append("indigenous women")
        text.append("and PSYDEH have")
        text.append("dismantled walls,")
        text.append("planted seeds and")
        text.append("dream of fruits")
        text.append("to come.")
        offset = 0
        offsetY = 0
        for frag in text:
            d.text((10, offsetY), frag[0:max(i - offset, 0)], font)
            offsetY += 40
            offset += len(frag)
        d.flush()
        return image

    @staticmethod
    def getPhrase37():
        font = aggdraw.Font("white", "sans.ttf", 28)
        texts = ["sustainable"]
        texts.append("economic")
        texts.append("development")
        return Phrases().makeImage_centered(texts, font)

    @staticmethod
    def getPhrase38():
        font = aggdraw.Font("white", "sans.ttf", 28)
        texts = [" education"]
        texts.append("that")
        texts.append("empowers")
        return Phrases().makeImage_centered(texts, font)

    @staticmethod
    def getPhrase39():
        font = aggdraw.Font("white", "sans.ttf", 28)
        texts = ["protected rights"]
        texts.append("and")
        texts.append("justice")
        return Phrases().makeImage_centered(texts, font)

    @staticmethod
    def getPhrase40():
        font = aggdraw.Font("white", "sans.ttf", 28)
        texts = ["healthy relations"]
        texts.append("between")
        texts.append("women and men")
        return Phrases().makeImage_centered(texts, font)

    @staticmethod
    def getPhrase41():
        font = aggdraw.Font("white", "sans.ttf", 28)
        texts = ["responsible"]
        texts.append("government")
        return Phrases().makeImage_centered(texts, font)

    @staticmethod
    def getPhrase42():
        font = aggdraw.Font("white", "sans.ttf", 28)
        texts = ["  protected"]
        texts.append("environment")
        return Phrases().makeImage_centered(texts, font)

    @staticmethod
    def getPhrase43():
        font = aggdraw.Font("white", "sans.ttf", 28)
        texts = ["quality"]
        texts.append("health")
        texts.append("care")
        return Phrases().makeImage_centered(texts, font)

    @staticmethod
    def getPhrase44():
        font = aggdraw.Font("white", "sans.ttf", 28)
        texts = ["umbrella network"]
        texts.append("of")
        texts.append("local NGOs")
        return Phrases().makeImage_centered(texts, font)

    @staticmethod
    def getPhrase45():
        font = aggdraw.Font("white", "sans.ttf", 28)
        texts = ["free, prior & informed"]
        texts.append("consent")
        texts.append("on land use")
        return Phrases().makeImage_centered(texts, font)

    @staticmethod
    def getPhrase46(i):
        image = Image.new("L", (1150, 405), "black")
        d = aggdraw.Draw(image)
        font = aggdraw.Font("white", "adler.ttf", 36)
        text = ["Still, as of May 2016, our tree is not strong enough"]
        text.append("to bear fruit. The foundation remains weak.")
        offset = 0
        offsetY = 0
        for frag in text:
            d.text((10, offsetY), frag[0:max(i - offset, 0)], font)
            offsetY += 40
            offset += len(frag)
        d.flush()
        return image

    @staticmethod
    def getPhrase47(i):
        image = Image.new("L", (1150, 605), "black")
        d = aggdraw.Draw(image)
        font = aggdraw.Font("white", "adler.ttf", 36)
        text = ["-Team up with these women leaders"]
        text.append(" and PSYDEH.")
        text.append("             ")
        text.append("-Support our first ever ")
        text.append(" Crowdfunding campaign.")
        offset = 0
        offsetY = 0
        for frag in text:
            d.text((10, offsetY), frag[0:max(i - offset, 0)], font)
            offsetY += 40
            offset += len(frag)
        d.flush()
        return image

    @staticmethod
    def getPhrase48(i):
        image = Image.new("L", (1150, 605), "black")
        d = aggdraw.Draw(image)
        font = aggdraw.Font("white", "adler.ttf", 36)
        text = ["While we pursue Mexican federal"]
        text.append("government aid, in-country politics")
        text.append("and economics tell us to reach out")
        text.append("to global citizens. We need help to")
        text.append("build our globally scalable model")
        text.append("for driving bottom-up")
        text.append("sustainable development. ")
        offset = 0
        offsetY = 0
        for frag in text:
            d.text((10, offsetY), frag[0:max(i - offset, 0)], font)
            offsetY += 40
            offset += len(frag)
        d.flush()
        return image

    @staticmethod
    def getPhrase49(i):
        image = Image.new("L", (1150, 605), "black")
        d = aggdraw.Draw(image)
        font = aggdraw.Font("white", "adler.ttf", 36)
        text = ["Our Campaign goal of $15,000usd will"]
        text.append("underwrite the production of 3 of the")
        text.append("13 critically important initiatives")
        text.append("in our two-year plan to strengthen")
        text.append("the tree: ")
        offset = 0
        offsetY = 0
        for frag in text:
            d.text((10, offsetY), frag[0:max(i - offset, 0)], font)
            offsetY += 40
            offset += len(frag)
        d.flush()
        return image

    @staticmethod
    def getPhrase50(i):
        image = Image.new("L", (1150, 605), "black")
        d = aggdraw.Draw(image)
        font = aggdraw.Font("white", "adler.ttf", 36)
        text = ["State-wide conference linking"]
        text.append("indigenous women who propose")
        text.append("solutions to politicians post")
        text.append("June 2016 elections.")
        offset = 0
        offsetY = 0
        for frag in text:
            d.text((10, offsetY), frag[0:max(i - offset, 0)], font)
            offsetY += 40
            offset += len(frag)
        d.flush()
        return image

    @staticmethod
    def getPhrase51(i):
        image = Image.new("L", (1150, 605), "black")
        d = aggdraw.Draw(image)
        font = aggdraw.Font("white", "adler.ttf", 36)
        text = ["An action-learning program where"]
        text.append("the Regional Cooperative of Artisans")
        text.append("incubate their own sustainable")
        text.append("organization.")
        offset = 0
        offsetY = 0
        for frag in text:
            d.text((10, offsetY), frag[0:max(i - offset, 0)], font)
            offsetY += 40
            offset += len(frag)
        d.flush()
        return image

    @staticmethod
    def getPhrase52(i):
        image = Image.new("L", (1150, 605), "black")
        d = aggdraw.Draw(image)
        font = aggdraw.Font("white", "adler.ttf", 36)
        text = ["A narrative development program with"]
        text.append("women leaders to help refine personal,")
        text.append("organizational and the movement's")
        text.append("narrative.")
        offset = 0
        offsetY = 0
        for frag in text:
            d.text((10, offsetY), frag[0:max(i - offset, 0)], font)
            offsetY += 40
            offset += len(frag)
        d.flush()
        return image

    @staticmethod
    def getPhrase53(i):
        image = Image.new("L", (910, 570), "black")
        d = aggdraw.Draw(image)
        font = aggdraw.Font("white", "adler.ttf", 36)
        text = ["PSYDEH:"]
        text.append("At the table with our rural")
        text.append("and indigenous partners")
        text.append("in Mexico to:")
        text.append("     ")
        text.append("-boost citizen participiation")
        text.append("     ")
        text.append("-improve human security")
        text.append("     ")
        text.append("-build resilience")
        text.append("     ")
        text.append("-support responsible government")
        offset = 0
        offsetY = 0
        for frag in text:
            d.text((10, offsetY), frag[0:max(i - offset, 0)], font)
            offsetY += 40
            offset += len(frag)
        d.flush()
        return image

    @staticmethod
    def getPhrase127(i):
        image = Image.new("L", (510, 60), "black")
        d = aggdraw.Draw(image)
        font = aggdraw.Font("white", "adler.ttf", 40)
        d.text((10, 0), "www.psydeh.com"[0:max(i, 0)], font)
        d.flush()
        return image

    def makeImage(self, listOfText, font):
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

# Phrases.getPhrase26(50).show()
