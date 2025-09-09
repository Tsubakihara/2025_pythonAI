# ファイル名: overload05.py
# ヒント: データベースのレコードを「==」と「%」で比較・操作できるようにしよう
# （例: value が文字列の長さで割り切れるか判定）

class Record:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def XXXXXXXXXXX(self, other):  # 「==」
        return self.key == other.key and self.value == other.value

    def XXXXXXXXXXX(self, other):  # 「%」
        return len(self.value) % other == 0

r1 = Record(1, "Alice")
r2 = Record(1, "Alice")
r3 = Record(2, "Bob")

print(r1 == r2)   # 期待値: True
print(r1 % 5)     # 期待値: True （"Alice" の長さ5で割り切れる）
print(r3 % 2)     # 期待値: True （"Bob" の長さ3は2で割り切れない→False）
