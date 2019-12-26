#from google.colab import drive
#drive.mount("/content/drive", force_remount=True)
#!ls "/content/drive/My Drive/ColabNotebooks/IT"
#drive.mount("/content/drive/my-drive/ColabNotebooks/IT", force_remount=True)
#from google.colab.patches import cv2_imshow

import cv2
#이미지를 로딩하고, 보여줍니다.

def resizing(image_path, person, spell, pixel=1000):
    image = cv2.imread("%s/%d_%d.jpg" % (image_path, person, spell))
    r = float(pixel)/image.shape[1]             # image.shape[1] = width
    dim = (pixel, int(image.shape[0]*r))   # image.shape[0] = height
    resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
    #cv2.imshow("resize",first_resized)
    #cv2.waitKey(0)
    return resized

image_path = "image"

for person in range(1,11):
    num=0
    for spell in range(1,7):
        w1, w2, h1, h2 = 0, 100, 3, 81
        # w1: 가로 자르기 시작하는 부분
        # w2: 가로 자르는 끝부분
        # h1: 세로 자르는 시작하는 부분
        # h2: 세로 자르는 끝부분
        first_resized = resizing(image_path, person, spell)
        for height in range(1,8):
            w1 = 0
            w2 = 100
            for width in range(1,10):
                num+=1
                cropping = first_resized[h1:h2, w1:w2]
                #cv2.imshow("crop",cropping)
                #cv2.waitKey(0)
                cv2.imwrite("img/%d/cropped_%d_%d_%d.jpg" % (spell, person, spell, num), cropping)
                w1 = w2 + 12
                w2 = w1 + 100
            h1 = h2 + 2
            h2 = h1 + 79
        num = 0