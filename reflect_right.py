import cv2
import sys

input_path = sys.argv[1]
output_path = sys.argv[2]

img = cv2.imread(input_path)
reflected = cv2.flip(img, 1)

cv2.imwrite(output_path, reflected)
