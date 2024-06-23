from PIL import Image, ImageDraw, ImageFont
import textwrap

SIZE = 65
TEXT = "\"When you change your thoughts, remember to also change your world.\"—Norman Vincent Peale"
FONT_PATH = "/usr/share/fonts/ShareTechMono/ShureTechMonoNerdFont-Regular.ttf"

text = textwrap.wrap(TEXT, width=20)

img = Image.open("test.jpg")
tobj = ImageDraw.Draw(img)
font = ImageFont.truetype(FONT_PATH, SIZE)

tobj.text(xy=(10, 10), text=TEXT, fill="#FF5000", font=font)

img.save("test2.jpg")
