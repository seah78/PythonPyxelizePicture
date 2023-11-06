import cv2
import time

import glob
import random



images = glob.glob('images/*.png')

# Input image
image = cv2.imread(random.choice(images))

# Get input size
height, width = image.shape[:2]

# Desired "pixelated" size
w, h = (1, 1)


# Resize input to "pixelated" size
temp = cv2.resize(image, (w, h), interpolation=cv2.INTER_LINEAR)

# Initialize output image
image_pyxelize = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)

# cv2.imshow('Input', image)
cv2.imshow('Output', image_pyxelize)

total_seconds = 60

while total_seconds > 0:
    if total_seconds > 5:
        interval_height = 1
        interval_width = 1
    else:
        interval_height = (height - h) / total_seconds
        interval_width = (width - w) / total_seconds
        
    h += int(interval_height)
    w += int(interval_width)
    temp = cv2.resize(image, (w, h), interpolation=cv2.INTER_LINEAR)
    image_pyxelize = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)
    time.sleep(1)
    total_seconds -= 1
    cv2.imshow('Output', image_pyxelize)
    if total_seconds > 0:
        cv2.waitKey(1)
    else:
        print("GAME OVER")






