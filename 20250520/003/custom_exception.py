# 問題：ユーザー定義例外と raise
# 年齢が負の場合に CustomError を発生させて処理します。

class CustomError(Exception):
    pass

def validate_age(age):
    if age < 0:
        raise XXXXXXXXX("年齢は0以上でなければなりません")
    else:
        print("年齢OK:", age)

try:
    validate_age(-1)
except CustomError as e:
    print("カスタムエラー処理:", e)
finally:
    print("バリデーション終了")

# 出力:
# カスタムエラー処理: 年齢は0以上でなければなりません
# バリデーション終了
