# 問題11: チャット画面を表示するルートを完成させてください。
# 実行方法: python chat_q1_basic_route.py → http://127.0.0.1:5001/chat にアクセス
# Flaskが返すHTMLに「チャット画面」と表示されることを確認してください。

from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/chat')
def chat():
    return render_template_string(XXXXXXXXX)

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(debug=True, port=5001)