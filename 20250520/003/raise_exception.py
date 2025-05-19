# 問題：raise を使って例外を送出する
# 負の数値を受け取った場合に ValueError を送出し、例外処理します。

def check_positive(number):
    if number < 0:
        raise XXXXXXXXX("負の値が渡されました")
    else:
        print("正の値です:", number)

try:
    check_positive(-5)
except ValueError as e:
    print("エラー処理:", e)
finally:
    print("チェック終了")

# 出力:
# エラー処理: 負の値が渡されました
# チェック終了
