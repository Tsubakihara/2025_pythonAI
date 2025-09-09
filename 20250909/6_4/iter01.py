# ファイル名: iter01.py
# ヒント: ログファイルを1行ずつ順に読み出せるイテレータを作ろう

class LogReader:
    def __init__(self, logs):
        self.logs = logs
        self.index = 0

    def XXXXXXXXXXX(self):  # __iter__
        return self

    def XXXXXXXXXXX(self):  # __next__
        if self.index < len(self.logs):
            line = self.logs[self.index]
            self.index += 1
            return line
        else:
            raise StopIteration

logs = ["[INFO] Start", "[WARNING] Low memory", "[ERROR] Crash detected"]
reader = LogReader(logs)

for log in reader:
    print(log)
# 期待値: 各ログが1行ずつ表示される
