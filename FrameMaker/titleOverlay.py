from PIL import Image
from Tools.frontender import languages


class title:
    def __init__(self, start, length, position):
        self.startTime = start
        self.stopTime = start + length
        self.title = Image.open("./images/title.png")
        self.position = position

    def draw(self, frame, image):
        if (frame < self.startTime or frame >= self.stopTime):
            return
        idx = frame - self.startTime
        if idx < 70:
            color = min(5 * (idx), 255)
        else:
            color = max(255 - 5 * (idx - 70), 0)
        mask = Image.new("L", self.title.size, color)
        image.paste(self.title, self.position, mask)

    def set_language(self, language):
        ':type language: languages'
        if language == languages.ENGLISH:
            self.title = Image.open("./images/title.png")
            print "title set to: English"
        elif language == languages.SPANISH:
            self.title = Image.open("./images/title_spanish.png")
            print "title set to: Spanish"
