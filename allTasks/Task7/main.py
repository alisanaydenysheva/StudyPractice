import cv2
import numpy as np

# load image
img = cv2.imread('defect.jpg')

# convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# adaptive threshold

thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, -35)

# apply morphology
kernel = np.ones((3,30),np.uint8)
morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
kernel = np.ones((3,35),np.uint8)
morph = cv2.morphologyEx(morph, cv2.MORPH_OPEN, kernel)

# get hough line segments
threshold = 25
minLineLength = 10
maxLineGap = 20
lines = cv2.HoughLinesP(morph, 1, 30*np.pi/360, threshold, minLineLength, maxLineGap)

# draw lines
linear1 = np.zeros_like(thresh)
linear2 = img.copy()
for [line] in lines:
    x1 = line[0]
    y1 = line[1]
    x2 = line[2]
    y2 = line[3]
    cv2.line(linear1, (x1,y1), (x2,y2), 255, 1)
    cv2.line(linear2, (x1,y1), (x2,y2), (0,0,255), 1)

print('number of lines:',len(lines))

# save resulting masked image
cv2.imwrite('scratches_thresh.jpg', thresh)
cv2.imwrite('scratches_morph.jpg', morph)
cv2.imwrite('scratches_lines1.jpg', linear1)
cv2.imwrite('scratches_lines2.jpg', linear2)

# display result
cv2.imshow("thresh", thresh)
cv2.imshow("morph", morph)
cv2.imshow("lines1", linear1)
cv2.imshow("lines2", linear2)
cv2.waitKey(0)
cv2.destroyAllWindows()
