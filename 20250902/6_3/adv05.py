# adv05.py
# ---------------------------------------------
# 問題5: 演算子オーバーロードで注文合計や比較を実装しよう
# ---------------------------------------------
# 【ポイント】
# ・__add__で注文金額を合算した新オブジェクトを返す
# ・__eq__で同額か比較
# ---------------------------------------------

class Order:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Order(self.amount + other.XXXXXXXXXXXX)

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
