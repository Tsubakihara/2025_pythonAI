import unittest

# 問題4: ショッピングカートの合計金額を計算する関数をテストする
# 商品ごとに price * quantity を合計する calculate_total をテストせよ。

def calculate_total(cart: list) -> int:
    return sum([item["price"] * item["quantity"] for item in cart])

class TestCart(unittest.TestCase):
    def test_cart_total(self):
        cart = [
            {"name": "pen", "price": 100, "quantity": 2},
            {"name": "notebook", "price": 200, "quantity": 1}
        ]
        self.assertEqual(XXXXXXXXXX, 400) # 正しい合計
        self.assertNotIn("eraser", XXXXXXXXXX) # カートに消しゴムは含まれない
        self.assertIsNotNone(XXXXXXXXXX) # 合計金額はNoneではない

if __name__ == "__main__":
    unittest.main()

# 実行コマンド:
# python -m unittest test_problem4.py
