# 業務報告書を読み込む処理です。
# ユーザーにファイルを選択してもらい、選択結果を確認メッセージとして表示してください。
# 選択されたファイルの拡張子が .csv でなければエラーメッセージを表示してください。

import FreeSimpleGUI as sg
import os

def select_report_file():
    file_path = sg.XXXXXXXXX("月次レポートファイルを選択してください", "レポート読込", "./reports")
    if not file_path:
        sg.popup("ファイルが選択されませんでした。")
        return
    if not file_path.endswith(".csv"):
        sg.popup_error("CSVファイルを選択してください。")
        return
    sg.popup_ok(f"ファイル {os.path.basename(file_path)} を読み込みます。")

select_report_file()
