import os
import tempfile
import wget
import random
import xml.etree.ElementTree as ET
import crop_random_portion as CRP
import tweet_image as TI

print("=== <START> signacbot ===")

# Get paintings library entries
tree = ET.parse("./pictures.xml")
root = tree.getroot()

# Choose random painting
number_of_paintings = len(list(root))
chosen_painting = random.randint(0, number_of_paintings-1)

painting_name    = root[chosen_painting].get('name')
painting_file    = root[chosen_painting].find('file').text
painting_painter = root[chosen_painting].find('painter').text
painting_year    = root[chosen_painting].find('year').text
painting_link    = root[chosen_painting].find('link').text

# Download painting
painting_download = "./downloaded_painting.jpg"

print(os.environ.get('PICTURES')) 
url = os.environ.get('PICTURES') + painting_file
wget.download(url, painting_download)

# Create temporary image of random portion
temp_file = tempfile.NamedTemporaryFile()

CRP.crop_random_portion(infile  = painting_download,
                        outfile = temp_file.name)

# Tweet out the temporary image with text
tweet_text = "'" + painting_name + "'" + \
             " by " + painting_painter + \
             " (" + painting_year + ") " + \
             painting_link + " #signac"

TI.tweet_image(text  = tweet_text,
               image = temp_file.name)

# Cleanup
os.remove(painting_download)
temp_file.close()

print("=== <END> signacbot ===")
