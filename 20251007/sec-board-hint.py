import os
import json
import hashlib
import datetime
from XXXXXXXX import request, make_response  # (1)
from flask.views import View
from cksession import CookieSession


class CookieSessionKai(CookieSession):
    """ セッション管理を行うクラス - 古いファイルを自動削除する機能付き """

    def __save_to_file(self):
        now = datetime.datetime.now().XXXXXXXX()  # (2)
        expired = now - 60 * 60 * 24 * 7  # 1週間前
        for fname in os.listdir(XXXXXXXX):  # (3)
            path = self.SESSION_DIR + "/" + fname
            mtime = os.path.getmtime(XXXXXXXX)  # (4)
            if mtime < expired:
                os.remove(XXXXXXXX)  # (5)
        path = self.SESSION_DIR + "/" + self.sid
        a_json = json.dumps(XXXXXXXX)  # (6)
        with open(path, "w", encoding="utf-8") as f:
            f.XXXXXXXX(a_json)  # (7)

    def save(self, response):
        response.set_cookie(self.SESSION_ID, self.sid)
        self.__save_to_file()


class SecBoardKai(View):
    USER_FILE = "sec-board-user-data.json"
    PASSWORD_SALT = "salt#xEiFiZJV3RIz0tMk#"
    ADMIN_USER = {"taro": "aaa", "jiro": "bbb"}

    def __init__(self):
        self.session = CookieSessionKai(request)
        if not os.path.XXXXXXXX(self.USER_FILE):  # (8)
            for user, pw in self.ADMIN_USER.XXXXXXXX():  # (9)
                self.__user_add(user, pw)

    def load_userinfo(self):
        userinfo = {}
        if os.path.exists(self.USER_FILE):
            with open(self.USER_FILE, "r") as f:
                userinfo = json.XXXXXXXX(f)  # (10)
        return XXXXXXXXX  # (11)

    def __user_add(self, user, pw):
        userinfo = self.load_userinfo()
        if user in XXXXXXXXX:  # (12)
            return False, self.make_error("ユーザーが既に存在します")
        pw2 = self.PASSWORD_SALT + pw
        hash = hashlib.sha256(XXXXXXXX.encode("utf-8")).hexdigest()  # (13)
        userinfo[XXXXXXXX] = hash  # (14)
        with open(self.USER_FILE, "w", encoding="utf-8") as f:
            json.XXXXXXXX(userinfo, f)  # (15)
        return True, None

    def user_add(self):
        if not self.XXXXXXXX():  # (16)
            return self.make_error("ログインが必要です")
        return self.make_html(
            "新規ユーザー登録",
            """
            <form method="POST" action="/XXXXXXXX">  <!-- (17) -->
            ユーザー名: <input type="text" name="user" size="8"><br>
            パスワード: <input type="password" name="pw" size="8">
            <input type="submit" value="新規作成">
            </form>
            """
        )

    def try_user_add(self):
        if not self.is_login():
            return self.make_error("ログインが必要です")
        user = request.form.get("XXXXXXXX", "")  # (18)
        pw = request.form.get("pw", "")
        ok, err = self.__user_add(user, pw)
        if not ok:
            return err
        return self.make_html("新規ユーザーを追加しました", "<a href='/sec'>戻る</a>")
