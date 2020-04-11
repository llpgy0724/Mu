import base64
import random
import string
from io import BytesIO

from PIL import Image, ImageDraw, ImageFont


def createImg(size=(160, 50)):
    bg_color = getRandomColor()
    img = Image.new(mode="RGB", size=size, color=bg_color)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font='../static/fonts/Arial.ttf', size=36)
    code = ''
    for i in range(4):
        random_txt = getRandomChar()
        txt_color = getRandomColor()
        code += random_txt
        while txt_color == bg_color:
            txt_color = getRandomColor()
        draw.text((10 + 30 * i, 3), text=random_txt, fill=txt_color, font=font)
    drawLine(draw)
    drawPoint(draw)
    print(img)
    f = BytesIO()
    img.save(f, "jpeg")
    data = f.getvalue()
    data = base64.b64encode(data).decode()
    return data, code


def drawLine(draw):
    for i in range(5):
        x1 = random.randint(0, 160)
        x2 = random.randint(0, 160)
        y1 = random.randint(0, 50)
        y2 = random.randint(0, 50)
        draw.line((x1, y1, x2, y2), fill=getRandomColor())


def drawPoint(draw):
    for i in range(50):
        x = random.randint(0, 160)
        y = random.randint(0, 50)
        draw.point((x, y), fill=getRandomColor())


def getRandomColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def getRandomChar():
    return random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)
