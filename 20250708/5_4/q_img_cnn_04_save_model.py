# ---------------------------------------------
# 問題4: モデルを保存し、読み込んで推論せよ
# 実行方法：ターミナルで以下を実行
# python q_img_cnn_04_save_model.py
# ---------------------------------------------

from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.utils import to_categorical
import numpy as np

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
model.fit(x_train, y_train, epochs=3)

# 保存
model.save("cnn_model.h5")

# 読み込み
loaded_model = XXXXXXXXX("cnn_model.h5")  # 読み込み関数を補完せよ

# 推論
pred = loaded_model.predict(x_test[:1])
print(pred)
