# sort_nested_dict_by_score.py
# -----------------------------
# 問題：
# 各人のスコア情報を持つ辞書を、"score" の値で降順に並び替えたリストを作成しなさい。
# XXXXXXXXX に適切なlambda式を記述しなさい。
# -----------------------------

students = {
    'John': {'score': 82, 'age': 21},
    'Alice': {'score': 91, 'age': 20},
    'Bob': {'score': 75, 'age': 23}
}

sorted_students = sorted(students.items(), key=XXXXXXXXX, reverse=True)

print(sorted_students)
# 出力例（順序のみを保証）:
# [('Alice', {'score': 91, 'age': 20}), ...]
