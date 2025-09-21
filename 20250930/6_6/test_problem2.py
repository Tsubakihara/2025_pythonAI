import unittest

# 問題2: ユーザーデータの検証関数をテストする
# 名前は文字列、年齢は18歳以上であることを確認する validate_user をテストせよ。

def validate_user(user: dict) -> bool:
    return isinstance(user.get("name"), str) and user.get("age", 0) >= 18

class TestUserValidation(unittest.TestCase):
    def test_user_validation(self):
        valid_user = {"name": "Taro", "age": 25}
        invalid_user = {"name": 123, "age": 15}
        self.assertTrue(XXXXXXXXXX)   # 正しいユーザーデータ
        self.assertFalse(XXXXXXXXXX)  # 年齢・型不正
        self.assertIsInstance(XXXXXXXXXX, dict) # ユーザーデータは辞書型である

if __name__ == "__main__":
    unittest.main()

# 実行コマンド:
# python -m unittest test_problem2.py
