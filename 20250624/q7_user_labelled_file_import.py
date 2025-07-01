# ユーザーに「処理ラベル名」として任意の文字列を入力してもらい、そのあとCSVファイルを選択して読み込みます。
# ファイルの先頭3行を表示し、ラベル名と一緒にログ出力してください。


import FreeSimpleGUI as sg

def load_labelled_csv():
    label = sg.XXXXXXXXX("処理ラベル名を入力してください（例：2025年度顧客）", "ラベル入力")
    if not label:
        sg.popup_error("ラベル名が未入力です。")
        return

    file_path = sg.XXXXXXXXX("CSVファイルを選択してください", "ファイル選択", "./data")
    if not file_path or not file_path.endswith(".csv"):
        sg.popup_error("CSVファイルが正しく選択されていません。")
        return

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            preview = "".join(lines[:3])
    except Exception as e:
        sg.popup_error(f"ファイル読込エラー: {str(e)}")
        return

    sg.popup_scrolled(f"【{label}】として読み込まれたデータの先頭3行：", preview)
    print(f"[{label}] ファイル：{file_path}")
    print("▼プレビュー▼")
    print(preview)

load_labelled_csv()
