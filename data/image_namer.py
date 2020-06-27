from skimage.io import imread
from skimage.io import imsave

lst = []
i = 0
for img_num in range(0, 816):
    try:
        # The given images may be in numerical order named
        image_path = '<file source>/' + (img_num) + '.jpg'
        img = imread(image_path)
        imsave('images/' + str(i) + '.jpg', img)
        i += 1
    except FileNotFoundError:
        # lst stores the missing images
        lst.append(img_num)
        continue
