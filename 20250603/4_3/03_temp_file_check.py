"""
【問題3】一時ファイルへの書き込みと内容検証

"temp.txt" に文字列を書き込んだあと、読み込み直して内容が正しいか検証する処理です。
ファイルの内容が期待通りであれば何も起きず、誤っていれば AssertionError が発生します。

XXXXXXXXXX に適切なコードを補完してください。
"""

with open("temp.txt", "w") as f:
    f.XXXXXXXXXX("temporary content")

with XXXXXXXXXX("temp.txt", "r") as f:
    content = f.read()

assert content == XXXXXXXXXX
