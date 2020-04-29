# from PIL import Image, ImageFilter

# img = Image.open('./pokemon/astro.jpg')
# img.thumbnail((400, 400))
# img.save('asro_resized.jpg')
# import sys
import os
from PIL import Image, UnidentifiedImageError
# sys.argv[1]
path = 'pokemon'
directory = 'new'
value = int(100)

try:
    if not os.path.exists(path):
        print("directory doesn't exists")
except FileNotFoundError as e:
    raise e
if not os.path.exists(directory):
    os.makedirs(directory)
try:
    add = 100 / len(os.listdir(path))
    value = 0
    for filename in os.listdir(path):
        img = Image.open(f'{path}/{filename}')
        img.thumbnail((value, value))
        img.save(f'{directory}/{filename}')
        value += add
except ZeroDivisionError as e:
    raise e
except UnidentifiedImageError as e:
    raise e
