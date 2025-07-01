# 社内システムのログイン処理として、ユーザーに「社員ID」の入力を促してください。
# 空入力の場合はエラーとし、正しく入力された場合はログを記録します。

import FreeSimpleGUI as sg

def login():
    user_id = sg.XXXXXXXXX("社員IDを入力してください", "ログイン認証")
    if not user_id:
        sg.popup_error("社員IDは必須項目です。")
        return
    sg.popup_ok(f"ログイン成功：ユーザーID [{user_id}]")
    print(f"[ログ] ユーザー {user_id} がログインしました。")

login()
