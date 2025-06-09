# ファイル名: question_1.py
# 問題: ログメッセージからユーザーIDを抽出してください。
# UserIDは "user_" に続く数字で構成されます。
# XXXXXXXXX を正しいコードに置き換えてください。

import re

log = "2025-06-09 18:22:01 - UserID: user_0345 logged in."
pattern = r"UserID:\s(user_\d+)"
match = re.search(pattern, log)

if match:
    print("User ID:", XXXXXXXXX)
