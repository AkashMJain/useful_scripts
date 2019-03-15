#!/usr/bin/env python

from __future__ import with_statement

from PIL import Image
import os
import argparse


# arguments declaration
ap = argparse.ArgumentParser()

ap.add_argument("-s", "--src", required=True, type=str, help="path to folder contening files")


args = vars(ap.parse_args())

'''
im = Image.open('Pictures/300x300.png')  # relative path to file
 im = Image.open('crop_dest/00002.jpg')
'''
emotions = 0
# Load gray scale image into variable
directory = os.fsencode(args["src"])
with open('output_file.csv', 'w+') as f:
    f.write('emotions, pixels\n')
    for file in os.listdir(directory):
        filename = args["src"] + os.fsdecode(file)

        im = Image.open(filename)

        # load the pixel info
        pix = im.load()

        # get a tuple of the x and y dimensions of the image
        width, height = 48, 48

        # open a file to write the pixel data
        # with open('output_file.csv', 'w+') as f:

        # f.write('R,G,B\n')

        # read the details of each pixel and write them to the file
        f.write('{0},'.format(emotions))
        for x in range(width):
            for y in range(height):
                gray = pix[x, y]
                # g = pix[x, x][1]
                # b = pix[x, x][2]
                f.write('{0} '.format(gray))
        f.write('\n')
