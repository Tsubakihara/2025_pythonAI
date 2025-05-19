# sort_list_of_dicts_by_name_length.py
# -----------------------------
# 問題：
# リスト内の辞書それぞれに "name" キーがあり、その文字列の長さ（len）で昇順に並び替えなさい。
# XXXXXXXXX に適切なlambda式を記述しなさい。
# -----------------------------

data = [
    {'name': 'Elizabeth', 'age': 29},
    {'name': 'Tom', 'age': 31},
    {'name': 'Charlotte', 'age': 27}
]

sorted_data = sorted(data, key=XXXXXXXXX)

print(sorted_data)
# 出力例:
# [{'name': 'Tom', ...}, {'name': 'Charlotte', ...}, ...]
