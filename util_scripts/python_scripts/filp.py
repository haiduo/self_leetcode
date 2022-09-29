import numpy as np
import PIL.Image as Image
import matplotlib.pyplot as plt
import cv2

img = Image.open("001010.jpg")
img1 = cv2.imread("001010.jpg")
img2=img.transpose(Image.FLIP_LEFT_RIGHT)       #左右对换
img3 = img1.copy()
img4 = img1.copy()
print(img1.shape)
for i in range(img1.shape[2]):
    img1[:, :, i] = np.fliplr(img1[:, :, i])
img1 = Image.fromarray(img1)

img4 = np.transpose(np.fliplr(np.transpose(img4, (2, 0, 1))), (1, 2, 0))
img4 = Image.fromarray(img4)

img3 = np.fliplr(img3)
img3 = Image.fromarray(img3)

img.show()
# img1.show()
# img2.show()
# img3.show()
img4.show()