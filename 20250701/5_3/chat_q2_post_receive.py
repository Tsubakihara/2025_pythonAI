# 問題12: チャットメッセージをPOSTで受信し、表示する処理を完成させてください。
# 実行方法: python chat_q2_post_receive.py → http://127.0.0.1:5002 にアクセスし、フォームで送信
# 入力した内容が画面に表示されることを確認してください。

from flask import Flask, request, render_template_string

app = Flask(__name__)

html = '''
<form method="post">
    メッセージ: <input type="text" name="msg">
    <input type="submit">
</form>
{% if message %}
<p><strong>あなたのメッセージ:</strong> {{ message }}</p>
{% endif %}
'''

@app.route('/', methods=['GET', 'POST'])
def chat():
    message = None
    if request.method == 'POST':
        message = request.XXXXXXXXX['msg']
    return render_template_string(html, message=message)

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(debug=True, port=5002)