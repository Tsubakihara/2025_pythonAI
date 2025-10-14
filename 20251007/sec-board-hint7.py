class CookieSessionKai(CookieSession):
    """ セッション管理を行うクラス - 古いファイルを自動削除する機能付き """
    def __save_to_file(self):
        # 古いセッションがあればここで削除する
        now = datetime.datetime.now().timestamp()
        expired = now - 60 * 60 * 24 * 7  # 1週間前を期限とする
        for fname in os.listdir(XXXXXXXX):  # (1)
            path = self.SESSION_DIR + "/" + fname
            mtime = os.path.getmtime(path)
            if mtime < expired:
                os.remove(XXXXXXXX)  # (2)
        # セッションデータを保存
        path = self.SESSION_DIR + "/" + self.sid
        a_json = json.dumps(self.values)
        with open(path, "w", encoding="utf-8") as f:
            f.write(XXXXXXXX)  # (3)

    def save(self, response):
        response.set_cookie(self.SESSION_ID, self.sid)
        self.__save_to_file()


class SecBoardKai(View):
    USER_FILE = "sec-board-user-data.json"
    PASSWORD_SALT = "salt#xEiFiZJV3RIz0tMk#"
    ADMIN_USER = {"taro": "aaa", "jiro": "bbb"}

    def __init__(self):
        self.session = CookieSessionKai(request)
        if not os.path.exists(XXXXXXXX):  # (4)
            for user, pw in self.ADMIN_USER.items():
                self.__user_add(user, pw)

    def __user_add(self, user, pw):
        userinfo = self.load_userinfo()
        if user in userinfo:
            return False, self.make_error("ユーザーが既に存在します")
        pw2 = self.PASSWORD_SALT + pw
        hash = hashlib.sha256(pw2.encode("utf-8")).hexdigest()
        userinfo[user] = hash
        with open(XXXXXXXX, "w") as f:  # (5)
            json.dump(XXXXXXXX, f)      # (6)
        return True, None

    def load_userinfo(self):
        userinfo = {}
        if os.path.exists(self.USER_FILE):
            with open(self.USER_FILE, "r") as f:
                userinfo = json.load(f)
        return XXXXXXXXX  # (7)
