#from google.colab import drive
#drive.mount("/content/drive", force_remount=True)
#!ls "/content/drive/My Drive/ColabNotebooks/IT"
#drive.mount("/content/drive/my-drive/ColabNotebooks/IT", force_remount=True)
#from google.colab.patches import cv2_imshow

import cv2
#이미지를 로딩하고, 보여줍니다.

image = cv2.imread("image/1_1.jpg")
r = 1000.0/image.shape[1]             # image.shape[1] = weight
dim = (1000, int(image.shape[0]*r))   # image.shape[0] = height
resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
cv2.imshow("resize",resized)
cv2.waitKey(0)


a = 0  # 가로 - 자르기 시작하는 부분
b = 100 # 가로 - 자르는 끝부분
c = 3  # 세로 - 자르는 시작하는 부분
d = 81 # 세로 - 자르는 끝부분
num = 0
for height in range(1,8):
    a = 0
    b = 100
    for weight in range(1,10):
        cropping = resized[c:d, a:b]
        cv2.imshow("cropping", cropping)
        cv2.waitKey(0)
        num = num + 1
        cv2.imwrite("img/cropped_1_1_" + str(num) + ".jpg", cropping)
            # 파일저장(img)폴더 안에, cropped_1_1_ = 첫번재 파일-가, cropped_1_2 = 첫번재 파일-나, 저장할때마다 바꿔줘야함. 함수쓰기 귀찮았어ㅎ
        a = b + 12
        b = a + 100
    c = d + 2
    d = c + 79
