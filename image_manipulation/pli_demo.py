from PIL import Image, ImageFilter
import os
image1 = Image.open('onepiece1.jpg')
image1.convert(mode='L').filter(ImageFilter.GaussianBlur(2)).save('onepiece_mod.jpg')