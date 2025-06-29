# 問題13: セッションを使ってチャットメッセージを保存し、会話履歴として表示してください。
# 実行方法: python chat_q3_session_log.py → http://127.0.0.1:5003 にアクセスし複数回送信して確認
# 複数のメッセージがリスト形式で表示されることを確認してください。

from flask import Flask, request, render_template_string, session
from flask import redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # セッション用の秘密鍵

html = '''
<form method="post">
    メッセージ: <input type="text" name="msg">
    <input type="submit">
</form>
<ul>
{% for m in messages %}
  <li>{{ m }}</li>
{% endfor %}
</ul>
'''

@app.route('/', methods=['GET', 'POST'])
def chat():
    if 'messages' not in session:
        session['messages'] = []

    if request.method == 'POST':
        msg = request.form['msg']
        session['messages'].append(msg)
        session.modified = True
        return redirect(url_for(XXXXXXXXX))

    return render_template_string(html, messages=session['messages'])

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(debug=True, port=5003)
