import numpy
from PIL import Image
from PIL import ImageOps


def find_coeffs(pa, pb):
    matrix = []
    for p1, p2 in zip(pa, pb):
        matrix.append([p1[0], p1[1], 1, 0, 0, 0, -p2[0] * p1[0], -p2[0] * p1[1]])
        matrix.append([0, 0, 0, p1[0], p1[1], 1, -p2[1] * p1[0], -p2[1] * p1[1]])

    A = numpy.matrix(matrix, dtype=numpy.float)
    B = numpy.array(pb).reshape(8)

    res = numpy.dot(numpy.linalg.inv(A.T * A) * A.T, B)
    return numpy.array(res).reshape(8)


def open_image(name, value):
    im = Image.new("RGBA", (1280, 720), "white")
    im2 = Image.open(name)
    im2 = im2.convert("L")
    im2 = ImageOps.invert(im2)
    im.paste((value, value, value), (0, 0), im2)
    return im


def getLetterRatio(text_a, text_b):
    len_a = 0
    len_b = 0
    for text in text_a:
        len_a += len(text)

    for text in text_b:
        len_b += len(text)

    return len_b / (1. * len_a)
