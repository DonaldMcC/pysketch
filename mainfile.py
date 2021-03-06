# https://medium.com/pythoneers/10-handy-automation-scripts-you-should-try-using-python-fc9450116938
# this will just implement the sketching approach and may then amend a bit

""" Photo Sketching Using Python """
import cv2

img = cv2.imread("donald.jpg")

# Image to Gray Image
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Gray Image to Inverted Gray Image
inverted_gray_image = 255 - gray_image

# Blurring The Inverted Gray Image
blurred_inverted_gray_image = cv2.GaussianBlur(inverted_gray_image, (19, 19), 0)

# Inverting the blurred image
inverted_blurred_image = 255 - blurred_inverted_gray_image

# Preparing Photo sketching
sketck = cv2.divide(gray_image, inverted_blurred_image, scale=256.0)

cv2.imshow("Original Image", img)
cv2.imshow("Pencil Sketch", sketck)
filename = 'sketch.jpg'

# Using cv2.imwrite() method
# Saving the image
cv2.imwrite(filename, sketck)

cv2.waitKey(0)
