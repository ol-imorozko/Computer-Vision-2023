import cv2
import sys

input_path = sys.argv[1]
output_path = sys.argv[2]

img = cv2.imread(input_path)
contrast_factor = 1.5

result = cv2.addWeighted(img, contrast_factor, np.zeros(img.shape, img.dtype), 0, 0)
cv2.imwrite(output_path, result)
