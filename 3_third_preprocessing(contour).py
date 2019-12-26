# 3. opencv contour : 이미지의 특성을 추출하여 더 명확하게 이미지를 인식하기 위함.

import cv2

def contour(image_path, person, spell, num):
    image = cv2.imread("%s%d_%d.jpg" %(image_path, person, num))
    imgray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thr = cv2.threshold(imgray, 70, 255, cv2.THRESH_BINARY)

    _, countors, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contour_img = cv2.drawContours(image, countors, -1, (0, 255, 0), 1)
    cv2.imwrite("final/%d/%d_%d.jpg" % (spell, person, num), contour_img)

image_path = "second_cropped"

for spell in range(1,7):
    for person in range(1, 11):
        for num in range(1,64):
            image_path = "second_cropped/%d/" %(spell)
            countoured = contour(image_path, person, spell, num)
            image_path2 = "final/%d" % (spell)

