# adv06.py
# ---------------------------------------------
# 問題6: 添え字アクセス可能な商品リストクラスを作成しよう
# ---------------------------------------------
# 【ポイント】
# ・__getitem__, __setitem__を実装しリストのラッパーを作る
# ---------------------------------------------

class ProductList:
    def __init__(self):
        self.products = []

    def __getitem__(self, index):
        return self.products[XXXXXXXXXXXX]

    def __setitem__(self, index, value):
        self.products[XXXXXXXXXXXX] = value

    def add_product(self, product):
        self.products.append(product)

plist = ProductList()
plist.add_product("Pen")
plist.add_product("Notebook")
plist.add_product("Eraser")

print(plist[1])  # Notebook

plist[1] = "Pencil"
print(plist[1])  # Pencil
