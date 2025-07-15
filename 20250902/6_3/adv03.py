# adv03.py
# ---------------------------------------------
# 問題3: 静的メソッドを使ってデータ検証ユーティリティを作成しよう
# ---------------------------------------------
# 【背景】
# 業務システムで頻繁に必要となるメールアドレスや電話番号などの形式チェック。
# 静的メソッドを使うことでインスタンス化せずに使える便利な検証クラスを作成します。
#
# 【今回学ぶポイント】
# ・@staticmethodデコレータの書き方と効果
# ・文字列の基本的な検証方法
#
# 【指示】
# ・is_emailメソッドに@staticmethodを付ける穴埋め
# ・メールアドレス判定の簡単なロジックを完成させる
# ・is_phoneメソッドの静的メソッド宣言を記述
# ・電話番号チェックの条件を穴埋め
# ・is_postal_codeメソッドの静的デコレータ穴埋め
# ・郵便番号検証のロジック穴埋め
# ・検証メソッドを呼び出して結果を表示
# ---------------------------------------------

class Validator:
    # 静的メソッドを示すデコレータを記述
    @XXXXXXXXXXXX  
    def is_email(email):
        # emailは文字列であること
        if not isinstance(email, str):
            return False
        # '@' と '.' が含まれているかチェック
        if '@' not in email or '.' not in email:
            return False
        # メールの長さが5文字以上であることを確認
        if len(email) < XXXXX:
            return False
        return True

    # is_phoneメソッドを静的メソッドとして宣言するデコレータを記述
    @XXXXXXXXXXXX
    def is_phone(number):
        # numberは文字列型かどうか判定
        if not isinstance(number, str):
            return False
        # 全て数字かどうか判定
        if not number.XXXXXXXXXXXX():
            return False
        # 桁数は10か11であることをチェック
        if len(number) not in (XXXXXXXXXXXX):
            return False
        return True

    # is_postal_codeメソッドを静的メソッドとしてデコレータを付ける
    @XXXXXXXXXXXX
    def is_postal_code(code):
        # codeは文字列であることを確認
        if not isinstance(code, str):
            return False
        # codeが数字のみで構成されているか判定
        if not code.XXXXXXXXXXXX():
            return False
        # 郵便番号は7桁かどうかを判定
        if len(code) != XXXXX:
            return False
        return True


print("メール判定（有効）:", Validator.is_email("test@example.com"))
print("メール判定（無効）:", Validator.XXXXXXXXXXXX("invalid-email"))  # 無効なメールでチェック
print("電話番号判定（有効）:", Validator.is_phone("09012345678"))
print("電話番号判定（無効）:", Validator.is_phone("abc123"))
print("郵便番号判定（有効）:", Validator.is_postal_code("1234567"))
print("郵便番号判定（無効）:", Validator.is_postal_code("123-4567"))
