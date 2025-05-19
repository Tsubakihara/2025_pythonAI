# lambda_map_conditional.py
# -----------------------------
# 問題：
# ある整数のリストが与えられたとき、各要素に対して以下の変換を行いなさい：
#   - 偶数なら2倍にする
#   - 奇数ならそのままにする
# lambda式と map() を使って、XXXXXXXXX の部分を埋めなさい。
# -----------------------------

numbers = [1, 2, 3, 4, 5, 6, 7]

result = list(map(lambda x: XXXXXXXXX if x % 2 == 0 else XXXXXXXXX, numbers))

print(result)
# 出力例: [1, 4, 3, 8, 5, 12, 7]
