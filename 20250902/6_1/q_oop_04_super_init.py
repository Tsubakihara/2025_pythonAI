# ---------------------------------------------
# 問題4: super() を使って親クラスの初期化を呼び出せ
# 実行方法: python q_oop_04_super_init.py
# ---------------------------------------------

# ヒント: 派生クラスでsuper().__init__()を使う

class Person:
    def __init__(self, name):
        self.name = name

class Employee(XXXXXXXXXXXX):
    def __init__(self, name, position):
        XXXXXXXXXXXX  # 親クラスの__init__呼び出し
        self.position = position

e = Employee("Alice", "Manager")
print(e.name, e.XXXXXXXXXXXX)
