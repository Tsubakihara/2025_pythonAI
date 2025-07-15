# ---------------------------------------------
# 問題8: 多重継承で複数の親クラスの機能を活用せよ
# 実行方法: python q_oop_08_multiple_inheritance.py
# ---------------------------------------------

class Flyer:
    def fly(self):
        return "Flying"

class Swimmer:
    def swim(self):
        return "Swimming"

class Duck(Flyer, XXXXXXXXXXXX):  # Swimmerを継承に追加
    pass

d = Duck()
print(d.XXXXXXXXXXXX())  # fly
print(d.XXXXXXXXXXXX())  # swim
