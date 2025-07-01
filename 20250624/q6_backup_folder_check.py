#ユーザーにバックアップ保存先のフォルダを選択してもらい、そのフォルダが存在しない場合は新規作成を促し、
# OKならフォルダを作成して続行する処理を作成してください。例外処理も含めて実装してください。

import FreeSimpleGUI as sg
import os

def select_backup_folder():
    folder_path = sg.XXXXXXXXX("バックアップ先のフォルダを選択してください", "フォルダ選択", "./backup")
    
    if not folder_path:
        sg.popup_error("フォルダが選択されていません。")
        return

    if not os.path.exists(folder_path):
        create = sg.popup_yes_no("選択されたフォルダは存在しません。作成しますか？", "確認")
        if create == "Yes":
            try:
                os.makedirs(folder_path)
                sg.popup_ok(f"フォルダ {folder_path} を作成しました。")
            except Exception as e:
                sg.popup_error(f"フォルダ作成エラー: {str(e)}")
                return
        else:
            sg.popup("バックアップ処理を中止しました。")
            return

    print(f"[バックアップ先]：{folder_path}")

select_backup_folder()
