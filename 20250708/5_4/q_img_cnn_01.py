# ---------------------------------------------
# 問題1: CIFAR-10画像データに対してCNNを構築し分類せよ
# 実行方法：ターミナルで以下を実行
# python q_img_cnn_01.py
# ---------------------------------------------

from tensorflow.keras.datasets import cifar10
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.utils import to_categorical

# データ準備
(x_train, y_train), (x_test, y_test) = cifar10.load_data()
x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# モデル構築
model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(XXXXXXXXX, activation='softmax'))  # 出力ユニット数を指定せよ

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# 学習
model.fit(x_train, y_train, batch_size=64, epochs=10, validation_split=0.2)

# 評価
loss, acc = model.evaluate(x_test, y_test)
print(f"Test Accuracy: {acc:.4f}")
