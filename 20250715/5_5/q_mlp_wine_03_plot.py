# ---------------------------------------------
# 問題3: モデルの損失と精度をグラフで可視化せよ
# 実行方法: python q_mlp_wine_03_plot.py
# plt.plot の項目を適切に指定し、学習曲線を表示してください。
# ---------------------------------------------

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical
import matplotlib.pyplot as plt

# データ準備
data = load_wine()
X = data.data
y = to_categorical(data.target)

X = StandardScaler().fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# モデル構築
model = Sequential([
    Dense(64, activation='relu', input_shape=(X.shape[1],)),
    Dense(64, activation='relu'),
    Dense(3, activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# 学習
history = model.fit(X_train, y_train, validation_split=0.2, epochs=30, batch_size=8)

# 可視化
plt.plot(history.history['XXXXXXXXX'], label='train')      # 損失 or 精度の key を指定せよ
plt.plot(history.history['val_XXXXXXXXX'], label='val')    # 検証用
plt.xlabel('Epoch')
plt.ylabel('Metric')
plt.legend()
plt.title('Learning Curve')
plt.show()
