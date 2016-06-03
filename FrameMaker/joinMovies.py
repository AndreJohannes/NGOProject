from PIL import Image

for i in range(0, 5000):
    im1 = Image.open("./frames/english/frame{}.png".format(i)).resize((640, 360), Image.ANTIALIAS)
    im2 = Image.open("./frames/spanish/frame{}.png".format(i)).resize((640, 360), Image.ANTIALIAS)

    image = Image.new("RGBA", (1280, 720), "black")
    image.paste(im1, (0, 180))
    image.paste(im2, (640, 180))
    print "saving frame {}".format(i)
    image.save("./frames/multi/frame{}.png".format(i), "png")
