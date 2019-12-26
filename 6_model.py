# 6. CNN 모델 구성

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
import numpy as np
import os
from keras.utils import to_categorical
from keras.callbacks import EarlyStopping
from keras.callbacks import ModelCheckpoint

np.random.seed(10)

# 데이터 준비
train_dataset = pd.read_csv('handwritten_train.csv')
train_dataset = train_dataset.values
valid_dataset = pd.read_csv('handwritten_valid.csv')
valid_dataset = valid_dataset.values
test_dataset = pd.read_csv('handwritten_test.csv')
test_dataset = test_dataset.values

# 데이터셋 분할
X_train = train_dataset[:,1:4097]
Y_train = train_dataset[:,4097]
X_valid = valid_dataset[:,1:4097]
Y_valid = valid_dataset[:,4097]
X_test = test_dataset[:,1:4097]
Y_test = test_dataset[:,4097]

# 모델 구성
model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=(64,64,1), padding='same'))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))
model.add(Conv2D(64, (4, 4), padding="same"))
model.add(Activation('relu'))
model.add(Conv2D(64, (3, 3)))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(units=11))
model.add(Activation('softmax'))

# 모델 학습과정 설정
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['acc'])

# X data image reshape
X_train = X_train.reshape(X_train.shape[0], 64, 64, 1)
X_valid = X_valid.reshape(X_valid.shape[0], 64, 64, 1)
X_test = X_test.reshape(X_test.shape[0], 64, 64, 1)

# One-hot encoding
data = np.array(Y_train)
data1 = np.array(Y_valid)
data2 = np.array(Y_test)

def encode(data):
    print('Shape of data (BEFORE encode): %s' % str(data.shape))
    encoded = to_categorical(data)
    print('Shape of data (AFTER  encode): %s\n' % str(encoded.shape))  # shape=11이 나오는 이유 -> index가 0부터 시작인데 값은 10까지 존재
    return encoded

Y_train = encode(data)
print(Y_train)
Y_valid = encode(data1)
print(Y_valid)
Y_test = encode(data2)
print(Y_test)


# 조기 종료 적용
callbacks_list = [
    EarlyStopping(
    monitor='val_acc',
    patience=35,
    ),
    ModelCheckpoint(
    filepath='handwritten_model.h5',
    monitor='val_loss',
    save_best_only=True)
]

# 모델 학습
hist = model.fit(X_train, Y_train, epochs = 200, batch_size = 20, callbacks=callbacks_list, validation_data=(X_valid, Y_valid))

# 모델 평가
scores = model.evaluate(X_test, Y_test)
print("%s: %.2f%%" %(model.metrics_names[1], scores[1]*100))

# 시각화
loss = hist.history['loss']
val_loss = hist.history['val_loss']
acc = hist.history['acc']
val_acc = hist.history['val_acc']

epochs = range(1, len(loss)+1)
plt.plot(epochs, loss, 'b', label='Training loss')
plt.plot(epochs, val_loss, 'g', label='Validation loss')
plt.plot(epochs, acc, 'y', label='Training accuracy')
plt.plot(epochs, val_acc, 'r', label='Validation accuracy')

plt.title('Training/Validation loss and accuracy')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()