# ファイル名: item05.py
# ヒント: 学生成績クラスを作り、科目名で点数を取得・更新できるようにする。

class GradeBook:
    def __init__(self):
        self.scores = {"Math": 80, "English": 70}

    def XXXXXXXXXXX(self, subject):  # get
        return self.scores.get(subject, "N/A")

    def XXXXXXXXXXX(self, subject, score):  # set
        self.scores[subject] = score

gb = GradeBook()
print(gb["Math"])    # 期待値: 80
gb["English"] = 85
print(gb["English"]) # 期待値: 85
print(gb["Science"]) # 期待値: N/A