# ---------------------------------------------
# 問題1: ワインデータセットを使ってMLPモデルを構築せよ
# 実行方法: python q_mlp_wine_01.py
# モデルの構造に適切なユニット数を指定し、精度を確認してください。
# ---------------------------------------------

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical

# データの読み込みと前処理
data = load_wine()
X = data.data
y = to_categorical(data.target)  # one-hot化

scaler = StandardScaler()
X = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# モデル構築
model = Sequential()
model.add(Dense(XXXXXXXXX, activation='relu', input_shape=(X.shape[1],)))  # 中間層ユニット数
model.add(Dense(3, activation='softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=20, batch_size=8, validation_split=0.1)

loss, acc = model.evaluate(X_test, y_test)
print(f"Test Accuracy: {acc:.4f}")
