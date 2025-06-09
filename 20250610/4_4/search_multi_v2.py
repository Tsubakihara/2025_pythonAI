# ファイル名: search_multi_v2.py
# 問題:
# キーワードが1つも指定されなければ終了し、複数キーワードをリスト化して検索する。
# `sys.argv[1:]` と `any(...)` を使って、複数条件での行抽出を完成させてください。

import os, sys

if len(sys.argv) <= 1:
    print("[USAGE] search_multi_v2 (keyword1 keyword2 ...)")
    XXXXXXXXX

keywords = XXXXXXXXX  # コマンドライン引数からキーワード一覧

for root, dirs, files in os.walk("."):
    for fi in files:
        path = os.path.join(root, fi)
        try:
            with open(path, encoding='utf-8') as f:
                for no, line in enumerate(f):
                    if XXXXXXXXX:  # 複数キーワードのいずれかを含むか？
                        print(f"{fi} ({no+1}): {line.strip()}")
        except:
            continue
