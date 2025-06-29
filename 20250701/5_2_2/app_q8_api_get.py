# 問題8: FlaskでREST APIエンドポイントを作成し、JSONでユーザー情報を返却せよ。
# 実行方法: python app_q8_api_get.py → curl http://127.0.0.1:5000/api/user にて確認
# 解答箇所: XXXXXXXXX を適切に埋めてください

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/user')
def get_user():
    user = {'id': 1, 'name': '田中次郎'}
    return XXXXXXXXX(user)

if __name__ == '__main__':
    app.run(debug=True)