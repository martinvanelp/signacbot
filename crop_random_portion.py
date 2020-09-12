import os
import random
from PIL import Image

# Open an image in RGB mode
print("...Opening image")

im = Image.open(r"./pictures/Paul_Signac_-_The_Port_of_Rotterdam_-_Google_Art_Project.jpg")

# Determine edges of random image portion:
print("...Calculating random edges")

image_size = im.size
portion_size = (480, 320)

left = random.randint(0, image_size[0]-portion_size[0]-1)
top  = random.randint(0, image_size[1]-portion_size[1]-1)

right  = left+portion_size[0]
bottom = top+portion_size[1]

# Cropped image with above edges
print("...Cropping image")

portion = im.crop((left, top, right, bottom))

# Save the portion as temporary image
print("...Saving temporary image")

outfile = "./tmp/temp.jpg"

if os.path.exists(outfile):
  os.remove(outfile)

portion.save(outfile, "JPEG")
