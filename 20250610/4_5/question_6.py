# ファイル名: question_6.py
# 問題: ログに含まれる IPv4 アドレス（形式: xxx.xxx.xxx.xxx）を "[REDACTED_IP]" に置換してください。
# ヒント: re.sub() を使用し、IPアドレスの正規表現は以下の形式を使用してください：
#         \b(?:\d{1,3}\.){3}\d{1,3}\b
# XXXXXXXXX を正しいコードに置き換えてください。

import re

log = "Access granted from 192.168.1.120 to internal resource."
pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
masked_log = XXXXXXXXX

print("Sanitized log:", masked_log)
