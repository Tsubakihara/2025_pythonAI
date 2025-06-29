# 問題7: Blueprintでルーティングを分離する構成を作成せよ。
# 実行方法: python app_q7_blueprint.py → http://127.0.0.1:5000/user で確認
# 必ず routes/user.py も同ディレクトリ内に作成してください。

from flask import Flask
from routes.user import user_bp

app = Flask(__name__)
app.register_blueprint(XXXXXXXXX, url_prefix='/user')

if __name__ == '__main__':
    app.run(debug=True)
