# ファイル名: item03.py
# ヒント: 在庫管理システムを作り、商品コードで数量を管理できるようにする。

class Inventory:
    def __init__(self):
        self.stock = {"A100": 50, "B200": 30}

    def XXXXXXXXXXX(self, code):  # get
        return self.stock.get(code, 0)

    def XXXXXXXXXXX(self, code, qty):  # set
        self.stock[code] = qty

inv = Inventory()
print(inv["A100"])  # 期待値: 50
inv["B200"] = 25
print(inv["B200"])  # 期待値: 25
