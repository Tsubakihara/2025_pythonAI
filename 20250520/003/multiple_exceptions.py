# 問題3：複数の例外処理と finally
# 値に応じてゼロ除算や無効な文字列変換をテストします。

def process(value):
    try:
        if value == "zero":
            1 / 0
        elif value == "bad":
            int("abc")
        else:
            print("処理成功:", value)
    except ZeroDivisionError:
        print("0での除算エラーです")
    except XXXXXXXXX:
        print("無効な数値変換です")
    finally:
        print("処理終了")

process("ok")
# 出力:
# 処理成功: ok
# 処理終了

process("zero")
# 出力:
# 0での除算エラーです
# 処理終了

process("bad")
# 出力:
# 無効な数値変換です
# 処理終了
