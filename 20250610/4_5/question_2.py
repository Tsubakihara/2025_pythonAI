# ファイル名: question_2.py
# 問題: 商品情報からカテゴリ名と価格を名前付きグループで抽出し、
# 辞書形式で出力してください。
# XXXXXXXXX を正しいコードに置き換えてください。

import re

product_info = "Category: Electronics, Price: 154000"
pattern = r"Category:\s(?P<category>\w+),\sPrice:\s(?P<price>\d+)"
match = re.match(pattern, product_info)

if match:
    result = XXXXXXXXX
    print("Parsed:", result)
