# 2. image second crop : 이미지를 더 깔끔하게 crop

import cv2

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


