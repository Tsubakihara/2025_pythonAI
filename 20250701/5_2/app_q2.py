# 問題2: URLパラメータで渡されたユーザー名を表示してください。
# 実行方法: python app_q2.py → http://127.0.0.1:5000/user/yourname にアクセス
# 解答箇所：XXXXXXXXX を適切に埋めてください

from flask import Flask

app = Flask(__name__)

@app.route('/user/<XXXXXXXXX>')


def show_user(username):
    return f'こんにちは、{username}さん！'

if __name__ == '__main__':
    app.run(debug=True)
