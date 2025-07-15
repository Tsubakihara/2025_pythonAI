# adv09.py
# ---------------------------------------------
# 問題9: 演算子オーバーロードで注文の合計や比較を可能にしよう
# ---------------------------------------------
# 【背景】
# 業務アプリで注文同士の合計金額計算や等価比較を自然に行いたい場合があります。
# 演算子オーバーロードを使い、+や==の動作を自作します。
#
# 【今回学ぶポイント】
# ・__add__で加算を実装
# ・__eq__で等価判定を実装
# ・型チェックも忘れずに行う
#
# 【指示】
# ・__add__のother.amount取得を穴埋め
# ・__eq__のother.amountとの比較を穴埋め
# ・新規Orderオブジェクト生成のコードを穴埋め
#

class Order:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        if not isinstance(other, Order):
            return NotImplemented
        total = self.amount + XXXXXXXXXXXX
        return XXXXXXXXXXXX(total)

    def __eq__(self, other):
        if not isinstance(other, Order):
            return False
        return self.amount == XXXXXXXXXXXX

    def __str__(self):
        return f"Order amount: {self.amount}"

o1 = Order(1000)
o2 = Order(2500)
o3 = o1 + o2
print(o3)
print("o1 == o2?", o1 == o2)
print("o1 == Order(1000)?", o1 == Order(1000))
