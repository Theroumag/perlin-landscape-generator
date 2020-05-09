from PIL import Image
import numpy as np
import random, noise

random.seed(0)
h = 480
w = 480

image = Image.new("RGB", (h, w))

for x in range(h):
    for y in range(w):
        c = int(random.random() * 255)
        # noise.pnoise2
        image.putpixel( (x,y), (c,c,c) )
image.save("map.png")
