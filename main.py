import cv2
from matplotlib import pyplot as plt

# Load images
img1 = cv2.imread('pohon 1.png')
img2 = cv2.imread('pohon 2.png')

# Resize gambar untuk memiliki ukuran yang sama
img1 = cv2.resize(img1, (600, 440))
img2 = cv2.resize(img2, (600, 440))

# Convert ke grayscale jika kedua gambar memiliki 3 channel
if img1.shape[2] == 3 and img2.shape[2] == 3:
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Compute difference image
diff = cv2.absdiff(img1, img2)

# Display input images and difference image
cv2.imshow('Input Image 1', img1)
cv2.imshow('Input Image 2', img2)
cv2.imshow('Difference Image', diff)

# Display histogram of difference image
hist = cv2.calcHist([diff], [0], None, [256], [0, 256])
plt.plot(hist)
plt.xlim([0, 256])
plt.title('Histogram of Difference Image')
plt.show()

# Save output image
cv2.imwrite('diff.jpg', diff)

# Wait for key press and then close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()