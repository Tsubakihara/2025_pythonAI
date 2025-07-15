# adv07.py
# ---------------------------------------------
# 問題7: イテレータを実装し社員リストをfor文で回せるようにしよう
# ---------------------------------------------
# 【背景】
# 業務アプリで社員名簿や顧客リストなどをfor文でシンプルに回せるようにするため、
# __iter__と__next__メソッドを使ってイテレータを実装します。
#
# 【今回学ぶポイント】
# ・__iter__は自身を返すこと
# ・__next__は現在の要素を返しつつインデックスを進めること
# ・全要素を返し終えたらStopIterationを送出すること
#
# 【指示】
# ・__iter__の戻り値を穴埋め
# ・__next__の条件判定・返却値・インデックス更新を穴埋め
# ・イテレータの状態を確認するためのメソッドを追加してください
#

class EmployeeList:
    def __init__(self, employees):
        self.employees = employees
        self.index = 0

    def __iter__(self):
        # イテレータの開始は自身を返す
        return XXXXXXXXXXXX

    def __next__(self):
        # インデックスが範囲外なら終了例外を送出
        if XXXXXXXXXXXX >= len(self.employees):
            raise StopIteration
        # 現在の要素を取得
        current_employee = self.employees[XXXXXXXXXXXX]
        # インデックスを1つ進める
        self.index = XXXXXXXXXXXX
        # 現在の社員名を返す
        return XXXXXXXXXXXX

    def reset(self):
        # インデックスを0に戻すメソッド
        self.index = 0

    def remaining(self):
        # まだ返していない社員数を返すメソッド
        return len(self.employees) - self.index

# 使用例
employees = EmployeeList(["Alice", "Bob", "Charlie", "Diana", "Evan"])
print("残りの社員数:", employees.remaining())

for emp in employees:
    print(emp)
print("残りの社員数:", employees.remaining())

employees.reset()
print("リセット後の残り社員数:", employees.remaining())

for emp in employees:
    print(emp)
