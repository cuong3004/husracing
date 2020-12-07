import cv2
import numpy as np
import matplotlib.pyplot as plt

whiteblankimage = 255 * np.ones(shape=[512, 512, 3], dtype=np.uint8)


cv2.rectangle(whiteblankimage, pt1=(100,200), pt2=(400,300), color=(0,0,255), thickness=10)

plt.imshow(whiteblankimage)

plt.show()
