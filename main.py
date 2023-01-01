import random
from PIL import Image

width = 64
length = 64

img = Image.new(mode="RGB", size=(width, length))

for x in range(width):
    for y in range(length):
        current = img.getpixel((x,y))
        new = (random.randint(1,256), random.randint(1,256), random.randint(1,256))
        img.putpixel((x,y), new)

img.save("image.png")