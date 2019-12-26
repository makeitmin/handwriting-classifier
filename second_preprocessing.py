import cv2
# 잘린 이미지들 -> 위아래 선 깔끔하게 하기 위함.
# from first_preprocessing import resizing

def cropping(image_path, person, spell, num):
    image = cv2.imread("%s_%d_%d_%d.jpg" %(image_path, person, spell, num))
    cropping = image[12:68, 7:95]
    cv2.imwrite("second_cropped/%d/%d_%d.jpg" %(spell, person, num), cropping)

image_path = "img"

for person in range(1,11):
    for spell in range(1,7):
        for num in range(1,64):
            image_path = "img/%d/cropped" %(spell)
            cropped=cropping(image_path, person, spell, num)
            image_path2 = "second_cropped/%d" % (spell)
            # resized=resizing(image_path2, person, num, 50)
            # cv2.imwrite("final/%d/%d_%d.jpg" %(spell, person, num), resized)

# GrayScale(나중에 혹시 사용할수도)
# dst = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
# cv2.imshow("src", resized)
# cv2.imshow("dst", dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()