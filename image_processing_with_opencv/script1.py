import cv2

img=cv2.imread("galaxy.jpg", 0)

print(len(img))
# returns 1485, as it is an array containing 1485 rows of pixels
print(img.shape)
#1485 X 990

# cv2.imshow("Galaxy", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# as they are will display an image that is too large for the screen

# resized_image=cv2.resize(img, (1000, 660))
# cv2.imshow("Galaxy", resized_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# appears on the screen at once but is misshapen because the ratio is off

scaled_image=cv2.resize(img, (int(img.shape[1] / 2), int(img.shape[0] / 2)))
cv2.imshow("Galaxy", scaled_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("Galaxy_resized.jpg", scaled_image)
