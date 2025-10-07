# クッキーを使ったセッション
import os, json
import datetime, random, hashlib

class CookieSession:
    """ クッキーを使ったセッションのクラス """
    
    SESSION_ID = "CookieSessionId"
    # セッションデータの保存先を指定 --- (*1) 
    SESSION_DIR = os.path.dirname(
        os.path.abspath(__file__)) + "/SESSION"

    def __init__(self, request):
        """ 初期化処理 """
        # セッションデータの保存パスを確認 --- (*2)
        if not os.path.exists(self.SESSION_DIR):
            os.mkdir(self.SESSION_DIR)

        # クッキーからセッションIDを得る --- (*3)
        self.sid = request.cookies.get(self.SESSION_ID, "")
        if self.sid == "":
            # 初回の訪問ならセッションIDを生成する
            self.sid = self.gen_sid()

        # 保存してあるデータを読み出す --- (*4)
        self.modified = False
        self.values = {}
        path = self.SESSION_DIR + "/" + self.sid
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                a_json = f.read()
                # JSON形式のデータを復元
                self.values = json.loads(a_json)

    def gen_sid(self):
        """ セッションIDを生成する """ # --- (*5)
        token = ":#sa$2jAiN"
        now = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
        rnd = random.randint(0, 100000)
        key = (token + now + str(rnd)).encode('utf-8')
        sid = hashlib.sha512(key).hexdigest()
        return sid

    def save(self, response):
        """ クッキーにセッションIDを設定 """ # --- (*6)
        response.set_cookie(self.SESSION_ID, self.sid)
        self.__save_to_file()

    def __save_to_file(self):
        """ セッションデータをファイルに書き出す """
        if not self.modified: return
        path = self.SESSION_DIR + "/" + self.sid
        # JSON形式に変換して保存
        a_json = json.dumps(self.values)
        with open(path, "w", encoding="utf-8") as f:
            f.write(a_json)

    # 添字アクセスのための特殊メソッドの定義 --- (*7)
    def __getitem__(self, key):
        return self.values[key]

    def __setitem__(self, key, value):
        self.modified = True
        self.values[key] = value

    def __contains__(self, key):
        return key in self.values

    def clear(self):
        self.values = {}
