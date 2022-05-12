import cv2  # python-opencv
import numpy as np


print("Координаты точки A(x1;y1):")
x1 = int(input("\tx1 = "))
y1 = int(input("\ty1 = "))

print("Координаты точки B(x2;y2):")
x2 = int(input("\tx2 = "))
y2 = int(input("\ty2 = "))

img = np.zeros((512, 512, 3), np.uint8)


cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3, cv2.LINE_8)
cv2.imshow("line", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Уравнение прямой, проходящей через эти точки:")
k = (y1 - y2) / (x1 - x2)
b = y2 - k*x2
print(" y = %.2f*x + %.2f" % (k, b))
