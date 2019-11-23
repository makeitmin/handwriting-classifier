import cv2

# 잘린 이미지들 -> 위아래 선 깔끔하게 하기 위함.

image = cv2.imread("img/cropped_1_1_13.jpg")
cropping = image[2:77, 2:98]
cv2.imshow("cropping", cropping)
cv2.waitKey(0)

# 픽셀 더 작게 수정
r = 50.0/cropping.shape[1]             # image.shape[1] = weight
dim = (50, int(cropping.shape[0]*r))   # image.shape[0] = height
resized = cv2.resize(cropping, dim, interpolation = cv2.INTER_AREA)
cv2.imshow("resize",resized)
cv2.waitKey(0)

def resize(image, window_height = 50):   # 이건 어디서 resize 함수 검색해서 바꾸려했는데 아직 못바꿈ㅎ..
    aspect_ratio = float(image.shape[1])/float(image.shape[0])
    window_width = window_height/aspect_ratio
    image = cv2.resize(image, (int(window_height),int(window_width)))
    return image

resize("img/cropped_1_1_1")

# GrayScale(나중에 혹시 사용할수도)
# dst = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
# cv2.imshow("src", resized)
# cv2.imshow("dst", dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()