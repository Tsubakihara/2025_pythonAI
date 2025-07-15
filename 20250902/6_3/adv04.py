# adv04.py
# ---------------------------------------------
# 問題4: 特殊メソッドでオブジェクトの文字列表現や呼び出し動作を実装しよう
# ---------------------------------------------
# 【ポイント】
# ・__str__, __repr__, __len__, __call__の使い方を学ぶ
# ・タスクのタイトルとサブタスク数を表示し、呼び出し時のメッセージを出す
# ---------------------------------------------

class Task:
    def __init__(self, title, subtasks):
        self.title = title
        self.subtasks = subtasks

    def __str__(self):
        return f"Task: {XXXXXXXXXXXX} with {len(self.subtasks)} subtasks"

    def __repr__(self):
        return f"Task(title={self.title!r}, subtasks={XXXXXXXXXXXX!r})"

    def __len__(self):
        return len(XXXXXXXXXXXX)

    def __call__(self):
        print(f"Starting task '{self.title}' with {len(self)} subtasks...")

t = Task("Prepare report", ["Write intro", "Analyze data", "Write conclusion"])

print(str(t))
print(repr(t))
print(len(t))
t()
