# ファイル名: question_4.py
# 問題: ログメッセージが "ERROR"、"WARN"、"INFO" のいずれかで始まっているかを検出し、
# そのレベルを抽出して出力してください。
# ヒント: re.match() + キャプチャグループ
# XXXXXXXXX を正しいコードに置き換えてください。

import re

log_entry = "ERROR: Disk failure at sector 2400"
pattern = r"^(ERROR|WARN|INFO):"
match = re.match(pattern, log_entry)

if match:
    level = XXXXXXXXX
    print("Log level:", level)
else:
    print("Log level not found.")
