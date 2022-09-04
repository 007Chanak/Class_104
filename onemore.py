import numpy as np
import cv2

# Create a black image
black = np.zeros([600,600])

black[200:400, 200:400] = 255
print(black)

cv2.imshow("black",black)
cv2.waitKey(0)