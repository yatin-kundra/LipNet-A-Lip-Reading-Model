import cv2 as cv

image = cv.imread('/AttractiveNet/SCUT-FBP5500_v2/Images/CF305.jpg')
# Get the dimensions of the image
# height, width, channels = image.shape

cv.imshow(image, (5,5))
# Loop through each pixel in the image
# for y in range(height):
#     for x in range(width):
#         # Get the RGB values of the pixel at (x, y)
#         blue = image[y, x, 0]
#         green = image[y, x, 1]
#         red = image[y, x, 2]