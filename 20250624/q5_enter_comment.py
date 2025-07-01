# カスタマーサポート対応後の業務記録として、対応内容をメモ形式で記録してください。
# 複数行の入力欄を表示し、記入内容をファイル出力用に整形して画面出力します。

import FreeSimpleGUI as sg

def input_support_memo():
    memo = sg.XXXXXXXXX("顧客対応内容を入力してください（200文字以内）", "対応記録入力", [60, 10])
    if not memo:
        sg.popup("内容が入力されていません。")
        return
    sg.popup("入力されたメモ内容を保存しました。")
    print("【保存内容】")
    print("-" * 40)
    print(memo)
    print("-" * 40)

input_support_memo()
