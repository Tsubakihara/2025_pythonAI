# ファイル名: overload03.py
# ヒント: 社員クラスで「<」と「>=」を使えるようにしよう（年齢で比較）

class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def XXXXXXXXXXX(self, other):  # 「<」
        return self.age < other.age

    def XXXXXXXXXXX(self, other):  # 「>=」
        return self.age >= other.age

e1 = Employee("Tanaka", 30)
e2 = Employee("Suzuki", 40)

print(e1 < e2)   # 期待値: True
print(e2 >= e1)  # 期待値: True
