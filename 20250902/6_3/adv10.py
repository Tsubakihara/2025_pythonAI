# adv10.py
# ---------------------------------------------
# 問題10: 添え字アクセスを可能にして商品リストを管理しよう
# ---------------------------------------------
# 【背景】
# 商品リストなどのデータ集合をクラスで管理しつつ、
# インデックスでアクセス・代入できるようにすることで扱いやすくします。
#
# 【今回学ぶポイント】
# ・__getitem__と__setitem__の実装
# ・リストのラップとデータ保持
#
# 【指示】
# ・__getitem__のindexアクセス部分を穴埋め
# ・__setitem__のindex指定と代入部分を穴埋め
# ・商品追加メソッドも適宜改良してください
#

class ProductList:
    def __init__(self):
        self.products = []

    def __getitem__(self, index):
        # 指定したインデックスの要素を返す
        return self.products[XXXXXXXXXXXX]

    def __setitem__(self, index, value):
        # 指定インデックスに値をセット
        self.products[XXXXXXXXXXXX] = value

    def add_product(self, product):
        # 新商品を追加
        self.products.append(product)

    def remove_product(self, product):
        # 商品をリストから削除（存在する場合）
        if product in self.products:
            self.products.remove(product)

    def list_all(self):
        # 現在の全商品を表示
        for idx, prod in enumerate(self.products):
            print(f"{idx}: {prod}")

plist = ProductList()
plist.add_product("Pen")
plist.add_product("Notebook")
plist.add_product("Eraser")

plist.list_all()

print(plist[1])  # Notebook

plist[1] = "Pencil"
print(plist[1])  # Pencil

plist.remove_product("Pen")
plist.list_all()
