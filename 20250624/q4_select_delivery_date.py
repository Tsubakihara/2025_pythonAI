# 出荷登録画面で、出荷予定日をユーザーに入力してもらう処理です。
# 日付は選択式ダイアログで入力できるようにしてください。
#  選択された日付は確認メッセージとして表示されます。

import PySimpleGUI as sg

def register_delivery_date():
    date = sg.XXXXXXXXX("出荷予定日を選択してください", "出荷日登録")
    if not date:
        sg.popup_error("出荷日が選択されていません。")
        return
    sg.popup_ok(f"出荷予定日：{date} を登録しました。")
    print(f"[ログ] 出荷日として {date} を登録。")

register_delivery_date()
