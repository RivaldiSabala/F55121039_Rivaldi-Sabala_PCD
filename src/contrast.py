import cv2

img = cv2.imread('jadiAbu.jpg')
cv2.normalize(img, img, alpha=100, beta=200, norm_type=cv2.NORM_MINMAX)
cv2.namedWindow('Test Window', cv2.WINDOW_AUTOSIZE)
cv2.imwrite('HasilContrastAbu.jpg', img)
cv2.imshow('Test', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
