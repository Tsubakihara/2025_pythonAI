# ファイル名: item02.py
# ヒント: 設定クラスを作り、キーでアクセス・更新できるようにする。

class Config:
    def __init__(self):
        self.settings = {"theme": "dark", "lang": "ja"}

    def XXXXXXXXXXX(self, key):  # get
        return self.settings[key]

    def XXXXXXXXXXX(self, key, value):  # set
        self.settings[key] = value

config = Config()
print(config["theme"])   # 期待値: dark
config["lang"] = "en"
print(config["lang"])    # 期待値: en
