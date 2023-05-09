import cv2
import numpy as np
print(cv2.__version__)

image = cv2.imread('test.jpg')
cv2.imshow('test.jpg',image)
cv2.waitKey(0)
cv2.destroyAllWindows()

(B, G, R) = cv2.split(image)
cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)
cv2.waitKey(0)
cv2.destroyAllWindows()

merged = cv2.merge([B,G,R])
merged[:,:,1]= np.zeros([merged.shape[0], merged.shape[1]])
cv2.imshow("Merged", merged)
cv2.waitKey(0)
cv2.destroyAllWindows()