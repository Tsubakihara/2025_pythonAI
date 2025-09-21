import unittest

# 問題3: 数列の合計値を返す関数をテストする
# 数列に負の値が含まれる場合は合計から除外する仕様とする。

def sum_positive(numbers: list) -> int:
    return sum([n for n in numbers if n >= 0])

class TestSumPositive(unittest.TestCase):
    def test_sum_positive(self):
        data = [10, -5, 20, -1, 15]
        self.assertEqual(XXXXXXXXXX, 45)  # 正しい合計値
        self.assertNotEqual(XXXXXXXXXX, 100) # 間違った合計値ではない
        self.assertIn(XXXXXXXXXX, data)   # リストに含まれる値を確認

if __name__ == "__main__":
    unittest.main()

# 実行コマンド:
# python -m unittest test_problem3.py
