# sort_dict_by_multiple_criteria.py
# -----------------------------
# 問題：
# 値に複数要素（得点と年齢）を持つ辞書を、まず得点（score）で降順、次に年齢（age）で昇順に並び替えなさい。
# XXXXXXXXX に適切なlambda式を記述しなさい。
# -----------------------------

people = {
    'Emma': {'score': 90, 'age': 30},
    'Liam': {'score': 90, 'age': 25},
    'Olivia': {'score': 85, 'age': 28}
}

sorted_people = sorted(people.items(), key=XXXXXXXXX)

print(sorted_people)
# 出力例:
# [('Liam', {'score': 90, 'age': 25}), ('Emma', {'score': 90, 'age': 30}), ...]
