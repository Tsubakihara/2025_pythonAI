# ---------------------------------------------
# 問題2: クラスとインスタンスの違いを理解せよ
# 実行方法: python q_oop_02_instance_vs_class.py
# ---------------------------------------------

# ヒント: クラス変数とインスタンス変数の使い分けに注目

class Dog:
    species = "Canis familiaris"  # クラス変数

    def __init__(self, name):
        self.name = XXXXXXXXXXXX  # インスタンス変数

dog1 = Dog("Pochi")
dog2 = Dog("Hachi")

print(dog1.XXXXXXXXXXXX)  # name
print(dog2.XXXXXXXXXXXX)  # name
print(Dog.XXXXXXXXXXXX)   # species
