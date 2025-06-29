# 問題5: Flaskのテンプレート機能（render_template_string）を使って、HTMLに変数を渡してください。
# 実行方法: python app_q5.py → http://127.0.0.1:5000 にアクセス
# 解答箇所：XXXXXXXXX を適切に埋めてください

from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def hello():
    user = '太郎'
    html = '''
    <html><body>
        <h1>こんにちは、{{ XXXXXXXXX }}さん！</h1>
    </body></html>
    '''
    return render_template_string(html, XXXXXXXXX=user)

if __name__ == '__main__':
    app.run(debug=True)
