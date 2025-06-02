# names は文字列のリスト、scores はキーが文字列、値が整数の辞書
# 戻り値は None としてください

from typing import List, Dict

def process_data(names: XXXXXXXXX, scores: XXXXXXXXX) -> XXXXXXXXX:
 for name in names:
  print(f"{name}: {scores.get(name, 0)}")
process_data(["Alice", "Bob"], {"Alice": 95})

# 例:
# process_data(["Alice", "Bob"], {"Alice": 95})
