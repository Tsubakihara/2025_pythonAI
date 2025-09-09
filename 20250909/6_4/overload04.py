# ファイル名: overload04.py
# ヒント: プロジェクトの進捗を「+」で合算し、「//」で進捗率を整数で出せるようにしよう

class Progress:
    def __init__(self, completed, total):
        self.completed = completed
        self.total = total

    def XXXXXXXXXXX(self, other):  # 「+」
        return Progress(self.completed + other.completed, self.total + other.total)

    def XXXXXXXXXXX(self, other):  # 「//」
        return (self.completed * 100 // self.total) // (other.completed * 100 // other.total)

    def __str__(self):
        return f"{self.completed}/{self.total}"

p1 = Progress(3, 10)
p2 = Progress(5, 15)
p3 = p1 + p2
print(p3)        # 期待値: 8/25
print(p1 // p2)  # 期待値: 0 （進捗率30% // 33%）
