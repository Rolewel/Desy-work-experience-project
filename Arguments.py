import argparse
from PIL import Image


parser = argparse.ArgumentParser(description='convert and save images')
parser.add_argument('-j', '--jpeg', action='store_true', help='convert image into jpeg')
parser.add_argument('-p', '--png', action='store_true', help='convert image into png')
arg = parser.parse_args()

def Image_Format()

if __name__ == '__main__':
    img = Image.open('Tiff_Test.tif')
    Format = Image_Format(args.jpeg, args.png)
    if arg.jpeg:
        img.save('Tiff.jpeg')
    elif arg.png:
        img.save('Tiff.png')


