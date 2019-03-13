#!/usr/bin/env python

from __future__ import with_statement
from PIL import Image

# im = Image.open('Pictures/300x300.png')  # relative path to file

im = Image.open('crop_dest/00002.jpg')

# load the pixel info
pix = im.load()

# get a tuple of the x and y dimensions of the image
width, height = im.size

# open a file to write the pixel data
with open('output_file.csv', 'w+') as f:
    f.write('gray\n')
    # f.write('R,G,B\n')

    # read the details of each pixel and write them to the file
    for x in range(width):
        for y in range(height):
            gray = pix[x, y]
            # g = pix[x, x][1]
            # b = pix[x, x][2]
            f.write('{0} '.format(gray))
