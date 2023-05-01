import cv2
import sys
import numpy as np

input_path = sys.argv[1]
output_path = sys.argv[2]

img = cv2.imread(input_path)
brightness_offset = 50

result = cv2.add(img, np.array([brightness_offset], dtype='uint8'))
cv2.imwrite(output_path, result)
