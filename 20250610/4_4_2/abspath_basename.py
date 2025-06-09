import os

# 問題 1: 絶対パスとファイル名の抽出
# ユーザーが指定した相対パス 'sample/test.txt' の絶対パスを求め、
# そこからファイル名部分のみを取り出して表示してください。

path1 = 'sample/test.txt'
abs_path = os.path.abspath(path1)
file_name = os.path.XXXXXXXX(abs_path)
print(f"問題1: ファイル名は '{file_name}' です。")
# 期待される出力例: ファイル名は 'test.txt' です。