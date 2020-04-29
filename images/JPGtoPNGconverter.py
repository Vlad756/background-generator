import sys
import os
from PIL import Image
import glob

folder = sys.argv[1]
new_folder = sys.argv[2]

if not os.path.exists(new_folder):
    os.mkdir(new_folder)

os.chdir(f'./{folder}')
for image in glob.glob("*.jpg"):
    name = os.path.splitext(image)[0]
    img = Image.open(image)
    img.save(f'../{new_folder}/{name}.png', 'PNG')
