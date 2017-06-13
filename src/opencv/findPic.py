#coding=utf-8
#pylint: disable=invalid-name
#pylint: disable=maybe-no-member
'''
查找图片
'''
import cv2
import time

img = cv2.imread('a.png', 0)
img2 = img.copy()
template = cv2.imread('b.png', 0)
w, h = template.shape[::-1]

# All the 6 methods for comparison in a list
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR', 'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
ticks = time.time()
for meth in methods:
    img = img2.copy()
    method = eval(meth)

    # Apply template Matching
    res = cv2.matchTemplate(img, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    print top_left, bottom_right, w, h
    cv2.rectangle(img, top_left, bottom_right, 255, 2)
    ticks2 = time.time()
    print ticks2 - ticks
    ticks = ticks2

cv2.imshow("Image", img)
cv2.waitKey(0)
