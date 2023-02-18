import cv2
import numpy as np
from PIL import Image
import pytesseract as tess

def recognize_text(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("binimg", gray)
    ret, binnary = cv2.threshold(gray, 100, 255, cv2.THRESH_OTSU)
    cv2.imshow("binmg", binnary)
    kerhel1 = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    bin1 = cv2.morphologyEx(binnary, cv2.MORPH_OPEN, kerhel1, iterations=1)
    kerhel2 = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 1))
    bin2 = cv2.morphologyEx(binnary, cv2.MORPH_OPEN, kerhel2, iterations=1)
    cv2.imshow("binary_img",bin2)
    text = tess.image_to_string(bin2)
    print("识别结果："%text)

img = cv2.imread('123.jpg',1)
recognize_text(img)
cv2.waitKey(0)
cv2.destroyAllWindows()

