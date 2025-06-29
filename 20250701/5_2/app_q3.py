# 問題3: クエリパラメータ name を取得して表示するWebページを作成してください。
# 実行方法: python app_q3.py → http://127.0.0.1:5000/greet?name=たろう にアクセス
# 解答箇所：XXXXXXXXX を適切に埋めてください

from flask import Flask, request

app = Flask(__name__)

@app.route('/greet')
def greet():
    name = request.XXXXXXXXX.get('name', 'ゲスト')
    return f'こんにちは、{name}さん！'

if __name__ == '__main__':
    app.run(debug=True)
