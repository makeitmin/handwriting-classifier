import cv2

# img = cv2.imread("C:/PythonProject/IT_TermProject/second_cropped/1/1_1.jpg")
#
# imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 이미지 gray컬러로 바꿈.
# ret, thr = cv2.threshold(imgray, 70, 255, cv2.THRESH_BINARY) # threshold사용 -> contour찾기
#
# _, countors, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # 이미지에서 찾는 contuours와 계층 구조 반환
# cv2.drawContours(img, countors, -1, (0, 255, 0), 1) # contours를 그리는 함수
#
# cv2.imshow('thr', thr)
# cv2.imshow('contours', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows() # 화면에 나온 윈도우 종료

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

