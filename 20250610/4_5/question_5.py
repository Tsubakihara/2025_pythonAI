# ファイル名: question_5.py
# 問題: CSV文字列から厳密なメールアドレスのみを抽出し、先頭と末尾のインデックスを表示してください。
# アドレス形式: [英数字+ドット]@[英数字+ドット].[ドメイン]
# ヒント: match.start() / match.end() を活用
# XXXXXXXXX を正しいコードに置き換えてください。

import re

csv_line = "1234, Tanaka Ichiro, tanaka.ichiro@example.com, Tokyo"
pattern = r"[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
match = re.search(pattern, csv_line)

if match:
    email = match.group()
    start_index = XXXXXXXXX
    end_index = XXXXXXXXX
    print("Email:", email)
    print("Start:", start_index, "End:", end_index)
