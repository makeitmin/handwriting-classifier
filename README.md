# 2019-2_DeepLearning-Project
Handwriting Distinction Project using CNN(Convolution Neural Network)

## Prerequsites
- Dataset
- Anaconda3 4.4.0 (Python 3.6)
- Tensorflow 1.15.0
- OpenCV 4.1.1.26
- Pandas 0.20.3
- Pillow(PIL) 4.1.1

## Run Files
1. first_preprocessing.py : crop raw image data
2. second_preprocessing.py : crop again because some first-cropped images includes black lines
3. third_preprocessing.py : use contour to make handwriting clear
4. preprocessing_division.py : divide second-cropped images by folders(train, valid, test)
5. preprocessing_csv.py : make second_cropped images 1 dimansional vector and put them into csv file
   -> handwritten_train.csv / handwritten_valid.csv / handwritten_test.csv
6. model.py : CNN model for learning
