import unittest

# 問題1: 商品の在庫管理システムの関数をテストする
# 在庫が十分ある場合はTrueを返し、足りない場合はFalseを返す関数 check_stock をテストせよ。
# 以下のXXXXXXXXXXを埋めよ。

def check_stock(stock: dict, item: str, quantity: int) -> bool:
    return stock.get(item, 0) >= quantity

class TestStock(unittest.TestCase):
    def test_stock_enough(self):
        stock = {"apple": 10, "banana": 5}
        self.assertTrue(XXXXXXXXXX)  # 在庫が足りる
        self.assertFalse(XXXXXXXXXX) # 在庫が足りない
        self.assertIsNone(XXXXXXXXXX) # 存在しない商品の場合はNoneになることを確認

if __name__ == "__main__":
    unittest.main()

# 実行コマンド:
# python -m unittest test_problem1.py
