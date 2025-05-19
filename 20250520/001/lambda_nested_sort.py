# lambda_nested_sort.py
# -----------------------------
# 問題：
# タプルのリストが与えられています。
# 各タプルは (名前, 年齢, 身長[cm]) を表します。
# 年齢で昇順、同じ年齢なら身長で降順に並べ替えるコードを完成させなさい。
# lambda式を使用して、XXXXXXXXX の部分を埋めなさい。
# -----------------------------

people = [
    ("Alice", 25, 160),
    ("Bob", 30, 175),
    ("Charlie", 25, 170),
    ("David", 30, 168),
    ("Eve", 22, 158)
]

sorted_people = sorted(people, key=lambda x: (XXXXXXXXX, -XXXXXXXXX))

print(sorted_people)
# 出力例: [('Eve', 22, 158), ('Charlie', 25, 170), ('Alice', 25, 160), ('David', 30, 168), ('Bob', 30, 175)]
