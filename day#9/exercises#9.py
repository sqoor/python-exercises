import statistics as st
import random
import math
from PIL import Image, ImageDraw, ImageFilter

# Q.1
x = [3, 1.5, 4.5, 6.75, 2.25, 5.75, 2.25]

print(st.mean(x))
print(st.harmonic_mean(x))
print(st.median(x))
print(st.median_low(x))
print(st.median_high(x))
print(st.median_grouped(x))
print(st.mode(x))
print(st.pstdev(x))
print(st.pvariance(x))
print(st.stdev(x))
print(st.variance(x))

# Q.2
print('Random Number: ', random.random())
print('Random range(10):', random.randrange(10))
print('Random choice:', random.choice(['Ali', 'Khalid', 'Hussam']))
print('Choose random letter form "Orange Academy":', random.choice('Orange Academy'))
print('Shuffle [1, 5, 8, 9, 2, 4]:', random.shuffle([1, 5, 8, 9, 2, 4]))
print('Generate random integer (from 20, 30):', random.randint(20, 30))
print('random.randrange[1000, 2111, 5]: ', random.randrange(1000, 2111, 5))
print('random.uniform(1, 10):', random.uniform(1, 10))

# Q.3
print('pi', math.pi)
print('cos(200), sin(30), tan(180)', math.cos(200), math.sin(30), math.tan(180))
print('floor(10.8)', math.floor(10.8))
print('ceil(10.8)', math.ceil(10.8))

# Q.4
image1 = Image.open('butterfly.jpg')
image2 = Image.open('desert.jpg')

# print(f'''
# image: {image1.format}
# format: {image1.size}
# size:{image1.mode}
# mode:
# ''')

# flipped_image = image1.transpose(Image.FLIP_TOP_BOTTOM)
# flipped_image.show()

# grey_image = image1.convert('L')
# grey_image.show()

# cropped_image = image1.crop((0, 0, 50, 50))
# cropped_image.show()

draw = ImageDraw.Draw(image1)
draw.line((0, 0) + image1.size, fill=(255, 255, 255))
draw.line((0, image1.size[1], image1.size[0], 0), fill=(255, 255, 255))
draw.text(
    (image1.size[0] / 2 - image1.size[0] / 2, image1.size[1] / 2 + 20),
    'Abdullah Al-Sqoor',
    fill=(255, 255, 0)
)

# image1.show()


edge_enhanced_image = image1.filter(ImageFilter.EDGE_ENHANCE)
find_edges = image1.filter(ImageFilter.FIND_EDGES)
smooth = image1.filter(ImageFilter.SMOOTH)
sharpen = image1.filter(ImageFilter.SHARPEN)


# edge_enhanced_image.show()
# find_edges.show()
# smooth.show()
# sharpen.show()


# blend
def changeImageSize(maxWidth,
                    maxHeight,
                    image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]

    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])

    newImage = image.resize((newWidth, newHeight))
    return newImage


image3 = changeImageSize(800, 500, image1)
image4 = changeImageSize(800, 500, image2)

image5 = image3.convert("RGBA")
image6 = image4.convert("RGBA")

blend = Image.blend(image5, image6, alpha=.2)
# blend.show()

# blur
blurred = image1.filter(ImageFilter.BLUR)
# blurred.show()

# rotate
image_rotate = image2.rotate(90)
# image_rotate.show()

# thumbnail
image2.thumbnail((128, 128))
image2.save('thumbnail.jpg')
# image2.show()


# composite
mask = Image.open('mask_circle.jpg').resize(image1.size)
Image.composite(image1, image2.resize(image1.size), mask).save('composite.jpg')
composite = Image.open('composite.jpg')
composite.show()
