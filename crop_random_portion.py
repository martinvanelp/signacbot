import random
from PIL import Image

def crop_random_portion(infile, outfile):
    print("--- <START> crop_random_portion ---")

    # Open an image in RGB mode
    print("    ...Opening image")

    im = Image.open(infile)

    # Determine edges of random image portion:
    print("    ...Calculating random edges")

    image_size = im.size
    width  = int(image_size[random.randint(0, 1)] * 0.1)
    height = int(image_size[random.randint(0, 1)] * 0.1)
    portion_size = (width, height)

    left = random.randint(0, image_size[0]-portion_size[0]-1)
    top  = random.randint(0, image_size[1]-portion_size[1]-1)

    right  = left+portion_size[0]
    bottom = top+portion_size[1]

    # Cropped image with above edges
    print("    ...Cropping image")

    portion = im.crop((left, top, right, bottom))

    # Save the portion
    print("    ...Saving image")

    portion.save(outfile, "JPEG")

    print("--- <END> crop_random_portion ---")

    return True
