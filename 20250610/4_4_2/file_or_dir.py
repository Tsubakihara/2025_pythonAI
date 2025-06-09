# problem3_file_or_dir.py

import os

# 問題 3: ファイルかディレクトリかの判定
# --------------------------------------
# 'data/sample.csv' がファイルかディレクトリかを判定し、
# 「これはファイルです」または「これはディレクトリです」と表示してください。
# 該当パスが存在しない場合はその旨を表示してください。

path3 = 'data/sample.csv'

if os.path.XXXXXXXX(path3):
    print("問題3: これはファイルです。")
elif os.path.XXXXXXXX(path3):
    print("問題3: これはディレクトリです。")
else:
    print("問題3: 該当するパスは存在しません。")
