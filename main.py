import cv2 as cv
import numpy as np

window_name = "Byoda"
img = cv.imread("./res/braintumor.jpg")
img2 = cv.imread('./res/braintumor.jpg')
img2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
cv.namedWindow(window_name)

wid = img2.shape[1]
hei = img2.shape[0]

drawing = False
ix = -1
iy = -1
x1 = 0
y1 = 0

def draw_rect(event, x, y, flags, param):
    global ix, iy, drawing, img, x1, y1
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix = x
        iy = y

    elif event == cv.EVENT_MOUSEMOVE:
        if drawing:
            img1 = cv.imread("./res/braintumor.jpg")
            cv.rectangle(img1, pt1=(ix, iy), pt2=(x, y), color=(0, 255, 255), thickness=1)
            print("ix = " + str(ix) + " and iy = " + str(iy) + "\n x = " + str(x) + " and y = " + str(y))
            img = img1
            x1 = x
            y1 = y

    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        img1 = cv.imread("./res/braintumor.jpg")
        cv.rectangle(img1, pt1=(ix, iy), pt2=(x, y), color=(0, 255, 255), thickness=1)
        img = img1
        x1 = x
        y1 = y

cv.setMouseCallback(window_name, draw_rect)

while True:
    cv.imshow(window_name, img)
    if cv.waitKey(10) == 13:
        break

for line in range(iy, y1):
    for col in range(ix, x1):
        if 125 <= img2[line, col] <= 180:
            img2[line, col] = img2[line, col]
        elif img2[line, col] < 125:
            img2[line, col] = 0
        elif img2[line, col] > 180:
            img2[line, col] = 0

imgB = np.zeros_like(img2)

for lineB in range(iy, y1):
    for colB in range(ix, x1):
        if (241 <= lineB <= 383) and (270 <= colB <= 384):
            imgB[lineB, colB] = 1
        elif (383 < lineB < 241) and (384 < colB < 270):
            imgB[lineB, colB] = 0

tensFinalImage = img2 * imgB
cv.imshow(window_name, tensFinalImage)
cv.waitKey()
cv.destroyAllWindows()
