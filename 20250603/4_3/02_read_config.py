"""
【問題2】設定ファイルの先頭行を読み込む

"config.txt" という設定ファイルを読み込み、1行目だけを取得する処理です。
取得後はファイルを閉じ、strip()で改行を取り除いた内容を表示してください。

XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX に適切なコードを補完してください。
"""

f = XXXXXXXXXX("config.txt", "r", encoding="utf-8")
first_line = f.XXXXXXXXXX()
f.XXXXXXXX()
print("設定ファイルの先頭行:", first_line.strip())
