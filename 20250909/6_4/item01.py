# ファイル名: item01.py
# ヒント: 部署ごとの社員リストを管理しよう。インデックスで社員名を取得・更新できるようにする。

class Department:
    def __init__(self, members):
        self.members = members

    def XXXXXXXXXXX(self, index):  # get
        return self.members[index]

    def XXXXXXXXXXX(self, index, value):  # set
        self.members[index] = value

dept = Department(["Tanaka", "Suzuki", "Kato"])
print(dept[0])     # 期待値: Tanaka
dept[1] = "Sato"
print(dept[1])     # 期待値: Sato
