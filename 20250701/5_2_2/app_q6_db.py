# 問題6: SQLAlchemyでユーザーデータベースを定義し、ユーザーを1人追加して表示するアプリを作成せよ。
# 実行方法: python app_q6_db.py
# 初回実行時に "users.db" が作成され、コンソールにユーザー名が表示されます。

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

@app.route('/')
def index():
    db.create_all()
    new_user = User(name='山田太郎')
    db.session.add(new_user)
    db.session.commit()
    user = User.query.XXXXXXXXX()
    return f"登録ユーザー: {user.name}"

if __name__ == '__main__':
    app.run(debug=True)
