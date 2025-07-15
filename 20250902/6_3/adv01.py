# adv01.py
# ---------------------------------------------
# 問題1: 非公開メンバでパスワードを安全に管理しよう
# ---------------------------------------------
# 【背景】
# 業務システムではユーザのパスワードを外部から直接変更されたり閲覧されたりすることは望ましくありません。
# そこでPythonの「非公開メンバ」を使って、外部からの不正アクセスを防ぎます。
#
# 【今回学ぶポイント】
# ・非公開メンバ（名前修飾 __varName）とは何か
# ・非公開メンバを安全に扱うためのメソッド設計
#
# 【指示】
# ・__password のように非公開メンバを定義してください。
# ・check_passwordメソッドでパスワードをチェックする処理を完成させてください。
# ・change_passwordメソッドで旧パスワードを検証してから新しいパスワードに変更してください。
#
# 以下のコードの穴埋めを埋めて実行してください。
# ---------------------------------------------

class User:
    def __init__(self, username, password):
        self.username = username
        self.XXXXXXXXXXXX = password  # 例: __password に変更

    def check_password(self, pw):
        # 入力されたパスワードと比較してTrue/Falseを返す
        return self.XXXXXXXXXXXX == pw

    def change_password(self, old_pw, new_pw):
        # 古いパスワードを検証し、合っていれば新しいパスワードに変更する
        if self.check_password(old_pw):
            self.XXXXXXXXXXXX = new_pw
            print("Password updated.")
        else:
            print("Old password incorrect.")

    def __get_password(self):
        # 非公開メソッド例（直接アクセスは不可）
        return self.XXXXXXXXXXXX

u = User("taro", "secret123")

print("ユーザ名:", u.username)
try:
    print("パスワード:", u.XXXXXXXXXXXX)  # 非公開なのでここはエラーになるはず
except AttributeError as e:
    print("エラー:", e)

print("パスワードチェック(pass='secret123'):", u.check_password("secret123"))
u.change_password("wrong", "newpass")  # 失敗パターン
u.change_password("secret123", "newpass")  # 成功パターン
print("新パスワードチェック(newpass):", u.check_password("newpass"))
