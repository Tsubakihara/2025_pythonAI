# 問題4: ジェネレータ式（難易度アップ）
# 1〜20の整数から、平方数（例: 1, 4, 9, 16, ...）だけを生成するジェネレータを作成してください。
# XXXXXXXXX の部分に適切な式を入れて完成させてください。

gen = (XXXXXXXXX for x in range(1, 21) if int(x**0.5)**2 == x)
print("問題4の答え:", list(gen))
# 期待される出力: [1, 4, 9, 16]
