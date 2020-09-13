import os
import random
import xml.etree.ElementTree as ET
import crop_random_portion as CRP

# Get paintings library entries
tree = ET.parse("./pictures/pictures.xml")
root = tree.getroot()

# Choose random painting
number_of_paintings = len(list(root))
chosen_painting = random.randint(0, number_of_paintings-1)

# print(root[chosen_painting].get('name'),
#       root[chosen_painting].find('file').text,
#       root[chosen_painting].find('link').text)

# Create temporary image of random portion
file = root[chosen_painting].find('file').text

tempfile = "./tmp/temp.jpg"

if os.path.exists(tempfile):
    os.remove(tempfile)

CRP.crop_random_portion("./pictures/" + file, tempfile)
