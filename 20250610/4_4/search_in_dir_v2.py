# ファイル名: search_in_dir_v2.py
# 問題:
# コマンドライン引数からディレクトリとキーワードを指定。
# 指定がなければ終了し、try-except 構文を補完してください。

import os, sys

if len(sys.argv) <= 2:
    print("[USAGE] search_in_dir_v2 (directory) (keyword)")
    XXXXXXXXX

target_dir = sys.argv[1]
keyword = sys.argv[2]

for root, dirs, files in os.walk(target_dir):
    for fi in files:
        path = os.path.join(root, fi)
        XXXXXXXXX:
            with open(path, encoding='utf-8') as f:
                for no, line in enumerate(f):
                    if keyword in line:
                        print(f"{path} ({no+1}): {XXXXXXXXX}")
        XXXXXXXXX:
            continue
