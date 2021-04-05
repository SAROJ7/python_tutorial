from PIL import Image
import os

size_300 = (300, 300)




for f in os.listdir('.'):
    if f.endswith('.jpg'):
        i = Image.open(f)         
        fn, ftext = os.path.splitext(f)
        i.thumbnail(size_300)
        i.save(f'300/{fn}_300{ftext}')

# with Image.open('onepiece1.jpg') as image1:
#     image1.show()
#     print(image1.format, image1.size, image1.mode)
#     image1.save('pup1.png')