# ファイル名: iter02.py
# ヒント: プロジェクトのタスクを順番に取り出せるイテレータを作ろう

class TaskList:
    def __init__(self, tasks):
        self.tasks = tasks
        self.position = 0

    def XXXXXXXXXXX(self):  # __iter__
        return self

    def XXXXXXXXXXX(self):  # __next__
        if self.position < len(self.tasks):
            task = self.tasks[self.position]
            self.position += 1
            return task
        else:
            raise StopIteration

tasks = TaskList(["Design", "Development", "Test", "Deploy"])
for t in tasks:
    print("Task:", t)
# 期待値: 各タスク名が順番に表示される
