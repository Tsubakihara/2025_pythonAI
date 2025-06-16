# 問題2: 集合型(set)内包表記
# 以下のリストから文字列の長さが3の単語の集合を作成してください。
words = ["cat", "dog", "bird", "ant", "cow", "owl"]
result_set = {XXXXXXXXX for w in words if len(w) == 3}
print("問題2の答え:", result_set)
# 期待される出力: {'cat', 'dog', 'ant', 'cow', 'owl'}