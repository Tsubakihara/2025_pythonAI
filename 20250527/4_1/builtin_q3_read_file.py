# ファイル "data.txt" に書かれたカンマ区切りの数値を読み込み、合計を計算する関数を完成させてください

def read_and_sum(filename: str) -> int:
 with XXXXXXXXX(filename, "r", encoding="utf-8") as f:
  content = f.read()
  numbers = [int(n) for n in content.XXXXXXXXX().XXXXXXXXX(",")]
  return sum(numbers)

# data.txt の内容例:
# 100,200,300
# → 結果: 600

