# ---------------------------------------------
# 問題7: クラスメソッドと静的メソッドを使い分けよ
# 実行方法: python q_oop_07_classmethod_staticmethod.py
# ---------------------------------------------

class Book:
    count = 0

    def __init__(self, title):
        self.title = title
        Book.count += 1

    @classmethod
    def get_count(cls):
        return XXXXXXXXXXXX

    @staticmethod
    def greet():
        return XXXXXXXXXXXX

b1 = Book("Python")
b2 = Book("AI")

print(Book.XXXXXXXXXXXX())  # クラスメソッド
print(Book.XXXXXXXXXXXX())  # 静的メソッド
