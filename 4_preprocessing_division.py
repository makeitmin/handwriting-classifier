# 4. 데이터 분할(6:2:2), "가~바"가 고르게 훈련셋/검증셋/시험셋에 분포하도록

import cv2

def set_path(count):
    top_path="distinction"
    if count > 51:
        bottom_path="test"
    elif count > 38:
        bottom_path="valid"
    else:
        bottom_path="train"
    image_path = top_path + "/" + bottom_path
    return image_path

for person in range(1, 11):
    for spell in range(1, 7):
        for num in range(1, 64):
            image = cv2.imread("second_cropped/%d/%d_%d.jpg" % (spell, person, num))
            path = set_path(num)
            print(path)
            cv2.imwrite("%s/%d/%d_%d.jpg" %(path, person, spell, num), image)

