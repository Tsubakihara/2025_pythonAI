# ---------------------------------------------
# 問題3: 基本的な継承を使って機能を拡張せよ
# 実行方法: python q_oop_03_inheritance_basic.py
# ---------------------------------------------

# ヒント: スーパークラスのメソッドをサブクラスで利用します

class Animal:
    def speak(self):
        return "Some sound"

class Cat(XXXXXXXXXXXX):  # Animalを継承
    def speak(self):
        return "Meow"

c = Cat()
print(c.XXXXXXXXXXXX())  # speakを呼び出し
