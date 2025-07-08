# ---------------------------------------------
# 問題3: EarlyStoppingを使いバリデーションロスの改善がないときに学習を停止せよ
# 実行方法：ターミナルで以下を実行
# python q_img_cnn_03_earlystopping.py
# ---------------------------------------------

from tensorflow.keras.datasets import cifar10
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.utils import to_categorical

(x_train, y_train), (x_test, y_test) = cifar10.load_data()
x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(64, activation='relu'),
    Dense(10, activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# EarlyStoppingコールバック
es = EarlyStopping(monitor='val_loss', patience=XXXXXXXXX, restore_best_weights=True)  # patienceを指定せよ

model.fit(x_train, y_train, epochs=50, batch_size=64, validation_split=0.2, callbacks=[es])
