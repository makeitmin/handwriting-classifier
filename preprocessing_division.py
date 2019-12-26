import cv2

def set_path(count): # train, valid, test 나눠서 넣을 폴더 경로 설정하는 함수 (6:2:2)
    top_path="distinction2"
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
            image = cv2.imread("second_cropped (1)/%d/%d_%d.jpg" % (spell, person, num))
            path = set_path(num)
            print(path)
            cv2.imwrite("%s/%d/%d_%d.jpg" %(path, person, spell, num), image)