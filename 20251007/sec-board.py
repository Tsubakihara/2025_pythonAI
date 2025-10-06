import os, html
from datetime import datetime
from flask import Flask, request, make_response
from flask.views import View
from cksession import CookieSession # 自作のセッションモジュール

#以下の機能を追加してください。
#- 新規ユーザを追加する仕組み
#- 定期的に古いセッションデータを削除する仕組み
#- 独自機能 + α

class SecBoard(View):
    """ 秘密のメッセージボードを実現するクラス """
    # ユーザ名とパスワード --- (*1)
    USERS = {"taro": "aaa", "jiro": "bbb"}
    # 秘密のメッセージを記述したファイル
    FILE_MSG = "sec-board-message-data.txt"
    # このビューで許可するHTTPメソッド
    methods = ['GET', 'POST']

    def __init__(self): # --- (*2)
        # セッションを開始
        self.session = CookieSession(request)

    def dispatch_request(self): # --- (*3)
        """リクエストを処理する"""
        # request.path からメソッド名を取得
        method_name = request.path.replace("/", "")
        # 指定されたメソッド名に対応するメソッドを取得し実行
        method = getattr(self, method_name, None)
        return method() if method else self.login()
 
    def make_html(self, title, body): # --- (*4)
        """ レスポンスを作成する """
        response = make_response(f"""
            <!DOCTYPE html><meta charset="utf-8"><html>
            <head><title>{title}</title></head><style>
            h1 {{ background-color: #eef; padding: 0.5em; }}
            </style><body><h1>{title}</h1>{body}</body>
            </html>""")
        self.session.save(response) # セッションを保存
        return response

    def make_error(self, msg):
        """ エラーを表示 """
        return self.make_html("エラー",
            f"<div style='color:red'>{msg}<div>")

    def login(self):
        """ ログイン画面を表示する """ # --- (*5)
        return self.make_html("ログイン", """
        <form method="POST" action="/try_login">
        ユーザ名: <input type="text" name="user" size="8"><br>
        パスワード: <input type="password" name="pw" size="8">
        <input type="submit" value="ログイン"></form>""")

    def try_login(self):
        """ ログイン可能か検証する """ # --- (*6)
        # フォームデータからログイン情報を得る
        user = request.form.get("user", "")
        pw   = request.form.get("pw", "")
        # ログインできるか調べる
        if (user not in self.USERS)or(self.USERS[user] != pw):
            return self.make_error("ユーザ名かパスワードが違います")
        # ログイン成功を明示
        self.session["login"] = datetime.now().timestamp()
        return self.make_html("ログイン成功",
            "<a href='/sec'>会員専用ボードを見る</a>")

    def logout(self):
        """ ログアウトする """ # --- (*7)
        self.session['login'] = 0
        return self.make_html('ログアウト', "<a href='/'>完了</a>")

    def is_login(self):
        """ ログインしているか判定する """ # --- (*8)
        return ("login" in self.session) and \
               (self.session['login'] > 0)

    def sec(self):
        """ 秘密のメッセージを表示する """ # --- (*9)
        if not self.is_login():
            return self.make_error("ログインが必要です")
        # 秘密のメッセージを読み込む
        msg = "(ここに秘密のメッセージを書いてください)" # 初期値
        if os.path.exists(self.FILE_MSG):
            with open(self.FILE_MSG, "r", encoding="utf-8") as f:
                msg = f.read()
        msg = html.escape(msg)
        return self.make_html("秘密のメッセージ", f"""
            <form method="POST" action="/sec_edit">
            <textarea name="msg" cols="70" rows="5">{msg}</textarea>
            <br><input type="submit" value="変更"></form>
            <hr><a href="/logout">→ログアウト</a>""")

    def sec_edit(self):
        """ 秘密のメッセージを編集する """ # --- (*10)
        if not self.is_login():
            return self.make_error("ログインが必要です")
        # 秘密のメッセージを保存して変更した旨を表示
        with open(self.FILE_MSG, "w", encoding="utf-8") as f:
            f.write(request.form.get("msg", ""))
        return self.make_html("変更", "<a href='/sec'>変更完了</a>")

# Flaskのオブジェクトを作成する --- (*11)
app = Flask(__name__)
# URLとメソッドを結びつける --- (*12)
board = SecBoard.as_view('board')
for path in ['/', '/login', '/try_login', '/logout', '/sec', '/sec_edit']:
    app.add_url_rule(path, view_func=board)

if __name__ == "__main__":
    app.run(debug=True, port=8080)
