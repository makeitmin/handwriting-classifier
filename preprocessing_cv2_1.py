#from google.colab import drive
#drive.mount("/content/drive", force_remount=True)
#!ls "/content/drive/My Drive/ColabNotebooks/IT"
#drive.mount("/content/drive/my-drive/ColabNotebooks/IT", force_remount=True)
#from google.colab.patches import cv2_imshow
import cv2
#이미지를 로딩하고, 보여줍니다.
image = cv2.imread("1-ga.jpg")
r = 1000.0/image.shape[1]
dim = (1000, int(image.shape[0]*r))
resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
cv2.imshow("resize",resized)
cv2.waitKey(0)
cv2.imwrite("thumbnail.png", resized)
count=0
a = 0
b = 140
list=[]
while count<8:
	count += 1
	cropping = resized[25:185, a:b]  # 높이를 100~200, 가로를 350~450 사이의 픽셀값을 cropping에 넣었습니다.
	list.append(cropping)
	cv2.imshow("cropping", cropping)
	a = b + 5
	b = a + 140
	cv2.waitKey(0)
print(len(list))