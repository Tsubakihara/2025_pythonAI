# ファイル名: search_logs_v2.py
# 問題:
# 引数が指定されていない場合に終了する処理（sys.exit）と、
# .log ファイルのみに絞る判定処理を埋めてください。

import os, sys

# 引数チェック
if len(sys.argv) <= 1:
    print("[USAGE] search_logs_v2 (keyword)")
    XXXXXXXXX

keyword = sys.argv[1]

for root, dirs, files in os.walk("."):
    for fi in files:
        if not fi.endswith(XXXXXXXXX):  # .log のファイルだけ対象
            continue
        path = os.path.join(root, fi)
        try:
            with open(path, encoding='utf-8') as f:
                for no, line in enumerate(f):
                    if keyword in line:
                        print(f"{fi} ({no+1}): {line.strip()}")
        XXXXXXXXX:
            continue
