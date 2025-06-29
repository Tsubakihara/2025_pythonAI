# 問題1: Flaskの基本的な構成を完成させてください。
# 実行方法: ターミナルで「python app_q1.py」と実行した後、http://127.0.0.1:5000 にアクセス
# 解答箇所：XXXXXXXXX を適切に埋めてください

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello Flask!'

if __name__ == '__main__':
    # Flaskアプリケーションの実行
    app.run(XXXXXXXXX=True)
    
