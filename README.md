# Desy-work-experience-project
Python script for image data analysis

from PIL import Image, ImageEnhance

img = Image.open('Logo_desy.png').convert('L')

enhancer = ImageEnhance.Contrast(img)
enhancer.enhance(5).save('image.png'
