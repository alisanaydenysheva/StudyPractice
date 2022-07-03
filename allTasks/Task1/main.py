import cv2 as cv
import numpy as np

def calculate():
    # Use a breakpoint in the code line below to debug your script.
    print("Координаты точки A(x1;y1):")
    x1 = int(input("\tx1 = "))
    y1 = int(input("\ty1 = "))

    print("Координаты точки B(x2;y2):")
    x2 = int(input("\tx2 = "))
    y2 = int(input("\ty2 = "))

    print("Координаты точки Ao(x1o;y1o):")
    x1o = int(input("\tx1o = "))
    y1o = int(input("\ty1o = "))

    print("Координаты точки Bo(x2o;y2o):")
    x2o = int(input("\tx2o = "))
    y2o = int(input("\ty2o = "))

    print("Уравнение прямой через эти точки:")
    if (x1-x2) == 0:
        k = 0
    else:
        k = (y1 - y2) / (x1 - x2)
    b = y2 - k * x2
    print(" y = %.2f*x + %.2f" % (k, b))
    y3 = k * x2o + b

    if y1o < y3 < y2o:
        print("объект вышел")
    elif y2o < y3 < y1o:
        print("объект вошел")
    else:
        print("прямая не пересечена")

    img = np.zeros((512, 512, 3), np.uint8)

    yl = k * 511 + b
    ylo = k * 0 + b
    if (x1-x2) == 0:
        k = 0
    else:
        xl = (511-b)/k



    cv.line(img, (0,int(ylo)), (511,int(yl)), (0,0,255), 2, cv.LINE_8)
    cv.line(img, (x1o,y1o), (x2o,y2o), (0,216,255), 2, cv.LINE_8)

    cv.imshow('line', img)
    cv.waitKey(0)

if __name__ == '__main__':
    calculate()
