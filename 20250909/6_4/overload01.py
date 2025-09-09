# ファイル名: overload01.py
# ヒント: 2Dベクトルクラスで「+」と「==」を実装しよう

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def XXXXXXXXXXX(self, other):  # 「+」を定義
        return Vector(self.x + other.x, self.y + other.y)

    def XXXXXXXXXXX(self, other):  # 「==」を定義
        return self.x == other.x and self.y == other.y

v1 = Vector(2, 3)
v2 = Vector(1, 5)
v3 = v1 + v2
print(f"({v3.x}, {v3.y})")   # 期待値: (3, 8)
print(v1 == Vector(2, 3))    # 期待値: True
