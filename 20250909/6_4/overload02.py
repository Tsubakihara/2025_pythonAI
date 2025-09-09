# ファイル名: overload02.py
# ヒント: 商品クラスで「==」と「!=」を使えるようにしよう（商品IDと名前で判定）

class Product:
    def __init__(self, product_id, name):
        self.product_id = product_id
        self.name = name

    def XXXXXXXXXXX(self, other):  # 「==」
        return self.product_id == other.product_id and self.name == other.name

    def XXXXXXXXXXX(self, other):  # 「!=」
        return not (self == other)

p1 = Product(101, "Keyboard")
p2 = Product(101, "Keyboard")
p3 = Product(202, "Mouse")

print(p1 == p2)  # 期待値: True
print(p1 != p3)  # 期待値: True
