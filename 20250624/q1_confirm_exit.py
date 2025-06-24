# 業務管理ツールを閉じようとした際に、「本当に終了しますか？」という確認ダイアログを表示し、
# ユーザーが「いいえ」を選択した場合には処理を中止してください。
# Tkinterのウィンドウを用いて、GUI画面上で処理している想定です。

import tkinter as tk
import PySimpleGUI as sg

def exit_application():
    confirm = sg.XXXXXXXXX("本当にアプリケーションを終了しますか？", "終了確認")
    if confirm == "No":
        print("終了処理がキャンセルされました。")
    else:
        print("アプリケーションを終了します。")
        root.destroy()

root = tk.Tk()
root.title("業務管理システム")
root.geometry("400x200")

exit_button = tk.Button(root, text="終了", command=exit_application)
exit_button.pack(pady=60)

root.mainloop()
