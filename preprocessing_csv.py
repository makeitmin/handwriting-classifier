import hashlib
from PIL import Image
import numpy as np
from preprocessing_shuffle import set_path
import pandas as pd
import csv
import os

# with open("img/cropped_1_1_1.jpg","rb") as file:    # 이미지 벡터화
#     string = file.read()
#     m = hashlib.md5()
#     m.update(string)
#     result = m.digest()
#     print(result)

def average_hash(fname, size=64):
    img = Image.open(fname) # 이미지 데이터 열기
    img = img.convert('L')  # 그레이 스케일
    img = img.resize((size,size), Image.ANTIALIAS) # resize
    pixel_data = img.getdata()  # 픽셀데이터
    pixels = np.array(pixel_data)   # 1차원 픽셀데이터
    # pixels = pixels.reshape((size,size))  # 2차원 픽셀데이터
    avg = pixels.mean() # 픽셀의 평균
    diff = 1 * (pixels > avg) # 픽셀 평균보다 크면 1, 작으면 0
    return diff

columns=[]

for i in range(4096):
    columns.append('pixel'+str(i))
columns.append('label')

# 두 이미지 비교해서 다른 픽셀 찾기 (16*16, 22개 다름 -> 거의 비슷)
#ahash_1 = average_hash('img/cropped_1_1_1.jpg')
#ahash_2 = average_hash('img/cropped_1_1_2.jpg')
#a = ahash_1.reshape(1, -1)
#b = ahash_2.reshape(1, -1)
#print((a != b).sum())

df1 = pd.DataFrame(index=np.arange(2280), columns=columns)
count=0
for person in range(1,11):
    for spell in range(1,7):
        for num in range(1,39):
            numpy_ahash = average_hash("distinction/train/%d/%d_%d.jpg" %(person, spell, num))
            list_ahash = numpy_ahash.tolist()
            labeled_ahash = np.array(list_ahash + [person])
            df1.loc[count] = labeled_ahash
            count+=1
            print(df1)
            df1.to_csv("handwritten_train.csv", index_label="index")

df2 = pd.DataFrame(index=np.arange(780), columns=columns)
count=0
for person in range(1,11):
    for spell in range(1,7):
        for num in range(39,52):
            numpy_ahash = average_hash("distinction/valid/%d/%d_%d.jpg" %(person, spell, num))
            list_ahash = numpy_ahash.tolist()
            labeled_ahash = np.array(list_ahash + [person])
            df2.loc[count] = labeled_ahash
            count+=1
            print(df2)
            df2.to_csv("handwritten_valid.csv", index_label="index")

df3 = pd.DataFrame(index=np.arange(720), columns=columns)
count=0
for person in range(1,11):
    for spell in range(1,7):
        for num in range(52,64):
            numpy_ahash = average_hash("distinction/test/%d/%d_%d.jpg" %(person, spell, num))
            list_ahash = numpy_ahash.tolist()
            labeled_ahash = np.array(list_ahash + [person])
            df3.loc[count] = labeled_ahash
            count+=1
            print(df3)
            df3.to_csv("handwritten_test.csv", index_label="index")