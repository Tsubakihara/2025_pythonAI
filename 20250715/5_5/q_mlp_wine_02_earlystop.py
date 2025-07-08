# ---------------------------------------------
# 問題2: EarlyStopping を使用して過学習を防げ
# 実行方法: python q_mlp_wine_02_earlystop.py
# patienceの値を適切に指定し、学習の最適タイミングを検出してください。
# ---------------------------------------------

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.callbacks import EarlyStopping

# データ前処理
data = load_wine()
X = data.data
y = to_categorical(data.target)

scaler = StandardScaler()
X = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

model = Sequential([
    Dense(64, activation='relu', input_shape=(X.shape[1],)),
    Dense(64, activation='relu'),
    Dense(3, activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# EarlyStopping
early_stop = EarlyStopping(monitor='val_loss', patience=XXXXXXXXX, restore_best_weights=True)  # patienceを指定せよ

model.fit(X_train, y_train, epochs=100, batch_size=8, validation_split=0.2, callbacks=[early_stop])

loss, acc = model.evaluate(X_test, y_test)
print(f"Test Accuracy: {acc:.4f}")
