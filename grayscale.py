import cv2
import sys

input_path = sys.argv[1]
output_path = sys.argv[2]

img = cv2.imread(input_path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imwrite(output_path, gray)
