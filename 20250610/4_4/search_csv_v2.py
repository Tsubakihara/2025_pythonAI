# ファイル名: search_csv_v2.py
# 問題:
# 検索結果を CSV ファイルとして保存する形式です。
# ファイルの書き込みモード、CSVの構造、strip処理などを埋めてください。

import os, sys, csv

if len(sys.argv) <= 1:
    print("[USAGE] search_csv_v2 (keyword)")
    XXXXXXXXX

keyword = sys.argv[1]

with open("results.csv", XXXXXXXXX, encoding='utf-8', newline='') as fout:
    writer = csv.writer(fout)
    writer.writerow(["File", "Line", "Text"])  # ヘッダー

    for root, dirs, files in os.walk("."):
        for fi in files:
            try:
                with open(os.path.join(root, fi), encoding='utf-8') as f:
                    for no, line in enumerate(f):
                        if keyword in line:
                            writer.writerow([fi, no+1, XXXXXXXXX])
            except:
                continue
