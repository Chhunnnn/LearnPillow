from PIL import Image, ImageFilter
import os

# os.listdir('.'): for current directory

print('1: ext: Change File Extension')
print('2: 300: Change Image Size')
print('3. rot: Rotate Left 90deg')
print('4. mode: Change To Monochrome')
print('4. blur: Make Image Blur')


act = input("Enter Number or Keyword: \n")

if act == 'ext':
    for f in os.listdir('Image'):
        if f.endswith('.jpg'):
            i = Image.open('Image/{}'.format(f))
            fn, fext = os.path.splitext(f)
            i.save('ImagePng/{}.png'.format(fn))
elif act == '300':
    size_300 = (300, 300)
    for f in os.listdir('Image'):
        i = Image.open('Image/{}'.format(f))
        fn, fext = os.path.splitext(f)
        i.thumbnail(size_300)
        i.save('300/{}_300{}'.format(fn, fext))
elif act == 'rot':
    for f in os.listdir('Image'):
        image = Image.open('Image/{}'.format(f))
        fn, fext = os.path.splitext(f)
        image.rotate(90).save('Rotated/{}_rotated.png'.format(fn))
elif act == 'mode':
    for f in os.listdir('Image'):
        image = Image.open('Image/{}'.format(f))
        fn, fext = os.path.splitext(f)
        image.convert(mode='L').save('Monochrome/{}_monochrome.png'.format(fn))
elif act == 'blur':
    for f in os.listdir('Image'):
        image = Image.open('Image/{}'.format(f))
        fn, fext = os.path.splitext(f)
        image.filter(ImageFilter.GaussianBlur(15)).save('Blur/{}_monochrome.png'.format(fn))


