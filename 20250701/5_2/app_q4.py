# 問題4: HTMLフォームで送信された名前をPOSTで受け取り、表示してください。
# 実行方法: python app_q4.py → ブラウザでフォームに名前を入力して送信
# 解答箇所：XXXXXXXXX を適切に埋めてください

from flask import Flask, request, render_template_string

app = Flask(__name__)

form_html = '''
<form method="post">
  名前: <input type="text" name="username">
  <input type="submit">
</form>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.XXXXXXXXX['username']
        return f'こんにちは、{name}さん！'
    return render_template_string(form_html)

if __name__ == '__main__':
    app.run(debug=True)