import unittest

# 問題5: ユーザーログイン認証を行う関数をテストする
# 正しいユーザーIDとパスワードの組み合わせの場合はTrueを返す。
# 間違っている場合はFalseを返す。

def authenticate(user_db: dict, user_id: str, password: str) -> bool:
    return user_db.get(user_id) == password

class TestAuth(unittest.TestCase):
    def test_authenticate(self):
        db = {"user1": "pass123", "user2": "abc456"}
        self.assertTrue(XXXXXXXXXX)  # 正しい認証
        self.assertFalse(XXXXXXXXXX) # 誤った認証
        self.assertIsNot(XXXXXXXXXX, None) # 戻り値がNoneではない

if __name__ == "__main__":
    unittest.main()

# 実行コマンド:
# python -m unittest test_problem5.py
